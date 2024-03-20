#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> CustomerDataType
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/21 03:49
@Desc   ：
==================================================
"""
import time

from faker.providers import BaseProvider


class CustomerDataType(BaseProvider):
    def unix_time_ms(self) -> int:
        return int(time.time() * 1000)
