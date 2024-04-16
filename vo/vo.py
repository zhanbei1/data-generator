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
import time
from typing import List

from pydantic import BaseModel, Field

from src.com_desmond.models.TaskModel import FieldConfig


class DataTypeVo(BaseModel):
    """
    数据类型VO
    """
    # 现实名称
    name: str
    # 类型描述
    description: str
    # 样例
    sample: str
    # 类型
    type: str
    # 额外参数
    args: List = Field(default=[])


class FieldTemplateVO(BaseModel):
    """
    字段模板
    """
    id: str = Field(default="")
    # 现实名称
    name: str = Field(default="")
    # 类型描述
    description: str = Field(default="")
    # 样例
    update_time: int = Field(default=None)
    # 类型
    create_time: int = Field(default=None)
    # 字段配置
    field_config: List[FieldConfig] = Field(default=[])
