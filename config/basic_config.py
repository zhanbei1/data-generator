#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> logger
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/18 18:15
@Desc   ：
==================================================
"""

# 日志格式
import logging
import os

LOG_FORMAT = "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.basicConfig(format=LOG_FORMAT)

# 日志存储路径
LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class GlobalBaseConfig:
    # 主节点的IP，默认也是8001端口
    data_generator_master_ip = "127.0.0.1"
    data_generator_master_port = 8001
    # 默认子节点的port
    data_generator_slave_port = 8002
    # 默认发送心跳频率
    slave_node_heart_interval = 5
    # 默认最大发送量
    task_default_max_data_num = 10000
    #  默认批次大小
    task_data_batch_size = 1000
    # 帮助文档默认目录
    helper_file_dir = "docs/"


class MasterNodeBaseConfig:
    port = 8001
