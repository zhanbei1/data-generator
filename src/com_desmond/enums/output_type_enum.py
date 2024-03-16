#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> output_type_enum
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/7 14:26
@Desc   ：支持的数据输出格式
==================================================
"""
from enum import Enum


class OutputTypeEnum(Enum):
    KAFKA = "kafka"
    FILE = "file"
