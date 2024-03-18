#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> test_amis
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/18 09:47
@Desc   ：
==================================================
"""


def test_task_list_amis():
    from amis.components import Page
    import json
    page = Page();

    with open('/Users/zhanbei/PycharmProjects/data-generator/html_json_config/task_config.json', 'r') as file:
        data = json.load(file)
        html = render(data)