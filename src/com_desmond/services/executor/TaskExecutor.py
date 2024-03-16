#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> TaskExecutor
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/7 13:53
@Desc   ：任务执行对象，每一个任务对应这样一个对象
==================================================
"""
from typing import List

from src.com_desmond.enums.DataTypeEnum import DataTypeEnum
from src.com_desmond.models.TaskModel import FiledConfig, TaskExecutorPlan


class TaskExecutor:
    tasks = {}

    @staticmethod
    def register_tasks(task_id: str, fields: List[FiledConfig]):
        print(f"TaskExecutor register_task {task_id}")
        TaskExecutor.tasks[task_id] = fields

    @staticmethod
    def unregister_task(task_id: str):
        TaskExecutor.tasks.pop(task_id)

    @staticmethod
    def execute(task_id: str, plan: TaskExecutorPlan) -> List[dict]:
        """
        执行生成数据的逻辑
        :return:
        """
        # 确定调度的执行时间，执行内产生日志的次数
        if TaskExecutor.tasks[task_id] is not None:
            result_data_list = []
            for n in range(plan.data_num):
                data_json = TaskExecutor._generate_data(TaskExecutor.tasks[task_id])
                result_data_list.append(data_json)
            return result_data_list
        else:
            raise ValueError("not found task id ......")

    @staticmethod
    def _generate_data(fields: List[FiledConfig]) -> dict:
        """
        生成数据的逻辑
        :return:
        """
        data_json = {}
        for filed in fields:
            data_json[filed.name] = DataTypeEnum.generator_by_key(filed.data_type)
        return data_json