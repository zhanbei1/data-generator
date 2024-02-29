#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> TaskModel
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/2/29 19:37
@Desc   ：执行生成数据的任务模型
==================================================
"""
from typing import List

from pydantic import BaseModel

from src.com_desmond.enums.DataDistributionEnum import DataDistributionEnum
from src.com_desmond.models.Fields import BaseField


class DataDistribution(BaseModel):
    """
    数据模型分布
    """
    distribution_type: DataDistributionEnum


class DataAnomaly(BaseModel):
    """
     数据异常模型分布
     """
    anomaly: List[BaseField]


class RangeFrequency(BaseModel):
    """
     生成数据的时间频率
     """
    # 时间范围【startTimestamp, endTimestamp】
    time_range: tuple[int, int]
    # 数据模型分布
    data_distribution: DataDistribution
    # 数据异常分布模型
    data_anomaly: DataAnomaly


class TaskModel(BaseModel):
    """
    执行生成数据的任务模型
    """
    name: str
    description: str
    range_frequency: RangeFrequency
    fields: List[BaseField]
