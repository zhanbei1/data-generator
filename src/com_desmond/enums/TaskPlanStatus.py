#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> TaskPlanStatus
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/16 14:16
@Desc   ：
==================================================
"""
from enum import Enum


class TaskPlanStatus(Enum):
    """
    任务计划状态
    """
    # 未开始
    NOT_STARTED = "not_start"
    # 进行中
    IN_PROGRESS = "pending"
    # 已完成
    COMPLETED = "success"
    # 执行失败
    FAILED = "0"
