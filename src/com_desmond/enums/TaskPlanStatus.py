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
    NOT_STARTED = "schedule"
    # 进行中
    IN_PROGRESS = "pending"
    # 已完成
    COMPLETED = "success"
    # 已取消
    CANCELLED = "fail"
    # 已过期
    EXPIRED = "0"
    # 已终止
    TERMINATED = "0"
    # 已暂停
    PAUSED = "0"
