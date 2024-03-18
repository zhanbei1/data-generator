#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> vo
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/19 03:00
@Desc   ：
==================================================
"""
from pydantic import BaseModel, Field


class DataTypeVo(BaseModel):
    """
    数据类型VO
    """
    # 现实名称
    name: str
    # 类型
    type: str
