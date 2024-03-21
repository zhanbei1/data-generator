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
    task_default_max_data_num = 10000
    task_data_batch_size = 1000

    helper_file_dir = "docs/"
