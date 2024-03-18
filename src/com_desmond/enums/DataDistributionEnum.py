#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> DataDistributionEnum
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/2/29 19:55
@Desc   ： 数据分布模型枚举
==================================================
"""
from src.com_desmond.models.TaskModel import RangeFrequency
from src.com_desmond.models.data_model import AllOutData, LinearData

from enum import Enum


class DataDistributionType:
    def __init__(self, data_distribution_type: str, data_type_class):
        self.dataDistributionType = data_distribution_type
        self.dataTypeClass = data_type_class

    def __str__(self):
        return self.dataDistributionType


class DataDistributionEnum(Enum):
    LINEAR = DataDistributionType("LINEAR", LinearData)
    ALL_OUT_DATA = DataDistributionType("ALL_OUT_DATA", AllOutData)

    @staticmethod
    def value_of(name: str):
        t = DataDistributionEnum[name]
        return t.value

    @staticmethod
    def getDataModelByKey(name: str, range_frequency: RangeFrequency):
        type_model: DataDistributionEnum = DataDistributionEnum.value_of(name)
        return type_model.dataTypeClass(range_frequency)
