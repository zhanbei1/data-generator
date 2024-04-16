#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> node
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/22 22:15
@Desc   ：
==================================================
"""
import socket
import threading
import time

import ujson

from config.basic_config import GlobalBaseConfig
from src.com_desmond.enums.TaskPlanStatus import TaskPlanStatus
from src.com_desmond.models.TaskModel import TaskModel
from src.com_desmond.services.engine.engine import GeneratorCoreEngine


class Node:
    def __init__(self):
        # 本机节点注册信息
        self.interval = GlobalBaseConfig.slave_node_heart_interval
        self.node_socket = self._init_socket()
        self.status = True

    def _init_socket(self) -> socket:
        port = GlobalBaseConfig.data_generator_slave_port
        node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # socket有效连接为心跳的2倍
        # self.socket.settimeout(self.interval * 2)
        node_socket.bind(("127.0.0.1", port))
        # self.socket.listen(5)
        # master 节点
        master_ip = GlobalBaseConfig.data_generator_master_ip
        master_port = GlobalBaseConfig.data_generator_master_port
        try:
            node_socket.connect((master_ip, master_port))
        except Exception as e:
            print("Node connect master error,  Continue reconnecting later: ")
        return node_socket

    def send_heartbeat(self):
        while self.status and threading.current_thread().is_alive():
            try:
                self.send_message_to_master("Heartbeat")
            except OSError as e:
                print("Node send_heartbeat error : " + e.__str__())
                try:
                    print(f"Node reconnecting...")
                    # socket有问题，关闭现有的socket，重新初始化socket
                    self.node_socket.close()
                    self.node_socket = self._init_socket()
                except OSError as e:
                    print("Node reconnect error : " + e.__str__())
            except KeyboardInterrupt or SystemExit as e:
                print("Node send_heartbeat KeyboardInterrupt | SystemExit : " + e.__str__())
                break
            time.sleep(self.interval)

    def send_message_to_master(self, message: str):
        self.node_socket.sendall(message.encode())

    def receive_messages(self):
        while self.status:
            try:
                # client_sock, client_addr = self.socket.accept()
                data = self.node_socket.recv(1048576)
                if data:
                    print(f"received data from master, data:{data}")
                    message = data.decode()
                    print(f"Received message from master: {message}")
                    task_list = ujson.loads(message)
                    for task in task_list:
                        task_model: TaskModel = TaskModel.model_validate(ujson.loads(task))
                        # 只有运行中的需要进行注册，其他情况可能是完成或者其他的情况，进行取消注册
                        if task_model.task_status != TaskPlanStatus.IN_PROGRESS.value:
                            GeneratorCoreEngine.unregister_task(task_model.id)
                        else:
                            GeneratorCoreEngine.register_task(task_model)
            except ConnectionResetError:
                print("Connection reset, removing connection")

    def close(self):
        self.node_socket.close()
        self.status = False
