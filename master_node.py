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
from typing import List

import ujson

from config.basic_config import MasterNodeBaseConfig
from database.sqllite3 import Session, session, Task
from src.com_desmond.enums.TaskPlanStatus import TaskPlanStatus
from src.com_desmond.models.TaskModel import TaskModel
from utils import db_task_to_model


class MasterNode:
    def __init__(self):
        port = MasterNodeBaseConfig.port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("127.0.0.1", port))
        self.socket.listen(5)
        # i+port : Node
        self.nodes = {}
        self.thread = None
        # 线程状态
        self.status = True

    def start_listening(self):
        def listen_for_connections():
            while self.status:
                try:
                    client_socket, client_address = self.socket.accept()
                    print(f"Accepted connection from {client_address}")
                    node = Node(client_address[0], client_address[1], client_socket)

                    self.nodes[str(client_address)] = node
                    result: List[Task] = session.query(Task).where(Task.task_status == TaskPlanStatus.IN_PROGRESS.name)
                    task_model_list = []
                    for task in result:
                        task_model: TaskModel = db_task_to_model(task)
                        task_model_list.append(task_model.json())
                    task_str_list: str = ujson.dumps(task_model_list)
                    client_socket.sendall(task_str_list.encode())
                except Exception as e:
                    print(f"Listen_for_connections error , error info {e}")

        self.thread = threading.Thread(target=listen_for_connections)
        self.thread.start()

    def broadcast_message(self, message):
        for address, node_socket in self.nodes:
            node_socket.sendall(message.encode())

    def close(self):
        self.socket.close()
        self.status = False


class Node:
    def __init__(self, address, port, conn):
        self.ip = address
        self.port = port
        self.client_socket_conn = conn
