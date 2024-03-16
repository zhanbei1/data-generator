#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> file_util
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/7 13:46
@Desc   ：
==================================================
"""
import hashlib


def file_md5(file_path: str) -> str:
    with(open(file_path, 'rb')) as f:
        md5_value = hashlib.md5(f.read()).hexdigest()
    return md5_value
