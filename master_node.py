#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> master_node
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/22 22:02
@Desc   ：作为master节点需要提供的接口内容
==================================================
"""
import socket
import threading
import time
from typing import List

import ujson

from config.basic_config import MasterNodeBaseConfig, GlobalBaseConfig
from database.sqllite3 import Session, session, Task
from src.com_desmond.enums.TaskPlanStatus import TaskPlanStatus
from src.com_desmond.models.TaskModel import TaskModel
from utils import db_task_to_model


class MasterNode:
    def __init__(self):
        port = MasterNodeBaseConfig.port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.interval = GlobalBaseConfig.slave_node_heart_interval
        self.socket.bind(("127.0.0.1", port))
        self.socket.listen(5)
        # i+port : Node
        self.nodes = {}
        self.listen_thread = None
        self.check_thread = None
        # 线程状态
        self.status = True

    def start_listening(self):
        def listen_for_connections():
            while self.status:
                try:
                    client_socket, client_address = self.socket.accept()
                    print(f"Accepted connection from {client_address}")
                    node: Node
                    if self.nodes.get(str(client_address), None) is not None:
                        node = self.nodes[str(client_address)]
                        node.flush_time = int(time.time() * 1000)
                    else:
                        client_socket.settimeout(self.interval + 2)
                        node = Node(client_address[0], client_address[1], client_socket)
                        self.nodes[str(client_address)] = node
                        result: List[Task] = session.query(Task).where(
                            Task.task_status == TaskPlanStatus.IN_PROGRESS.name)
                        task_model_list = []
                        for task in result:
                            task_model: TaskModel = db_task_to_model(task)
                            task_model_list.append(task_model.json())
                        task_str_list: str = ujson.dumps(task_model_list)
                        client_socket.sendall(task_str_list.encode())
                except Exception as e:
                    print(f"Listen_for_connections error , error info {e}")

        def check_for_connections():
            """
            检查是否有连接失效，关闭连接
            :return:
            """
            while self.status:
                try:
                    delete_key = []
                    for k, v in self.nodes.items():
                        # 接受消息，如果接受不到消息认为node节点不发心跳，同时判断时间，过了就剔除掉
                        v: Node
                        data = v.client_socket_conn.recv(1024)
                        if data:
                            print(f"Receive heart data from {k}")
                            v.flush_time = int(time.time() * 1000)

                        if int(time.time() * 1000) - v.flush_time > 1000 * (self.interval * 3):
                            delete_key.append(k)
                    # 删除所有过期的key
                    for del_key in delete_key:
                        v: Node = self.nodes[del_key]
                        if v.client_socket_conn:
                            v.client_socket_conn.close()
                        del self.nodes[del_key]
                        print(
                            f"Will close socket {v.ip}:{v.port}, last_flush time is {v.flush_time}, now is {int(time.time() * 1000)}")

                except Exception as e:
                    print(f"Check_for_connections error , error info {e}")
                time.sleep(self.interval)

        self.listen_thread = threading.Thread(target=listen_for_connections)
        self.listen_thread.start()
        self.check_thread = threading.Thread(target=check_for_connections)
        self.check_thread.start()

    def broadcast_message(self, message):
        for address, node_socket in self.nodes.items():
            node_socket.client_socket_conn.sendall(message.encode())

    def close(self):
        self.socket.close()
        self.status = False
        for node in self.nodes.values():
            node.client_socket_conn.close()


class Node:
    def __init__(self, address, port, conn):
        self.ip: str = address
        self.port: int = port
        self.flush_time: int = int(time.time() * 1000)
        self.client_socket_conn: socket = conn
