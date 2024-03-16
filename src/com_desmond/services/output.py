#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> output.py
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/8 18:16
@Desc   ：
==================================================
"""
from typing import List

from src.com_desmond.enums.output_type_enum import OutputTypeEnum
from src.com_desmond.models.TaskModel import OutputConfig
from src.com_desmond.services.output_models import BaseOutputModel, KafkaOutputModel, FileOutputModel


class Output:
    tasks = {}

    @staticmethod
    def register_output(task_id: str, config: OutputConfig):
        print(f"Output register_task {task_id}")
        if config.output_type == OutputTypeEnum.KAFKA:
            Output.tasks[task_id] = KafkaOutputModel(config.kafka_output)
        else:
            Output.tasks[task_id] = FileOutputModel(config.file_output)

    @staticmethod
    def unregister_task(task_id: str):
        output: BaseOutputModel = Output.tasks.pop(task_id)
        output.close()

    @staticmethod
    def output(task_id: str, data_list: List[str | dict]):
        output_model: BaseOutputModel = Output.tasks.get(task_id)
        output_model.send_data_list(data_list)
