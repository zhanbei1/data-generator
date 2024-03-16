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
    NOT_STARTED = 1
    # 进行中
    IN_PROGRESS = 2
    # 已完成
    COMPLETED = 3
    # 已取消
    CANCELLED = 4
    # 已过期
    EXPIRED = 5
    # 已终止
    TERMINATED = 6
    # 已暂停
    PAUSED = 7
