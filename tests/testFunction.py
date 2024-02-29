#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> testFunction
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/2/29 14:15
@Desc   ：
==================================================
"""
from faker import Faker

if __name__ == '__main__':
    faker = Faker("it_IT")
    print(faker.name())
