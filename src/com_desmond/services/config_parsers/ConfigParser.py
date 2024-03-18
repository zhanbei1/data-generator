#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> ConfigParser
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/2/29 19:09
@Desc   ：将指定的字符串转为对应的可执行的对象
==================================================
"""
from src.com_desmond.utils.file_util import file_md5
from src.com_desmond.models.TaskModel import TaskModel


class ConfigParser:

    @staticmethod
    def analysis_by_file_path(file_path: str) -> TaskModel:
        with(open(file_path, 'r', encoding='utf-8')) as f:
            md5_id = file_md5(file_path)
            task = ConfigParser.analysis_by_str_text(f.read())
            task.id = md5_id
            task.file_path = file_path
            return task

    @staticmethod
    def analysis_by_str_text(config_str: str) -> TaskModel:
        return ConfigParser.translate_to_task(config_str)

    @staticmethod
    def translate_to_task(task_conf: str) -> TaskModel:
        try:
            return TaskModel.model_validate_json(task_conf)
        except Exception as e:
            raise e
