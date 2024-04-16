#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> test_fields
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/8 20:25
@Desc   ：测试数据生成
==================================================
"""
from src.com_desmond.enums.DataTypeEnum import DataTypeEnum
from src.com_desmond.models.TaskModel import FieldConfig


def test_generator_data():
    test_config = """
    {
      "name": "desmond_test",
      "data_type": "ADDRESS",
      "extra_config": {}
    }
    """
    field_config = FieldConfig.parse_raw(test_config)
    data_json = {
        field_config.name: DataTypeEnum.generator_by_key(field_config.data_type)
    }
    print(data_json)


def test_data_type():
    t = DataTypeEnum.value_of("ADDRESS")
    print(t)
