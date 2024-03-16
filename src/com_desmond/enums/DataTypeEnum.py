#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> DataTypeEnum
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/6 16:43
@Desc   ：支持的数据类型枚举
==================================================
"""

from faker import Faker
from enum import Enum

fake = Faker()


class DataType:
    def __init__(self, name: str, function):
        self.name = name
        self.function = function


class DataTypeEnum(Enum):
    ADDRESS = DataType("ADDRESS", fake.address)
    NAME = DataType("NAME", fake.name)
    IPV4_PUBLIC = DataType("IPV4_PUBLIC", fake.ipv4_public)
    IPV6 = DataType("IPV6", fake.ipv6)
    HTTP_METHOD = DataType("HTTP_METHOD", fake.http_method)
    URL = DataType("URL", fake.url)
    CHROME = DataType("CHROME", fake.chrome)
    FIREFOX = DataType("FIREFOX", fake.firefox)
    DATE_TIME_THIS_YEAR = DataType("DATE_TIME_THIS_YEAR", fake.date_time_this_year)

    @staticmethod
    def value_of(name: str):
        t = DataTypeEnum[name]
        return t.value

    @staticmethod
    def generator_by_key(name: str):
        type_model: DataType = DataTypeEnum.value_of(name)
        return str(type_model.function())


if __name__ == '__main__':
    print(DataTypeEnum.ADDRESS)
    print(DataTypeEnum.value_of("ADDRESS"))
