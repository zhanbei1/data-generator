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
    def execute(task_id: str, plan: TaskExecutorPlan) -> list[dict]:
        """
        执行生成数据的逻辑
        :return:
        """
        # 确定调度的执行时间，执行内产生日志的次数
        if TaskExecutor.tasks[task_id] is not None:

            # TODO： 如果 plan.data_num = -1，默认一直发送，默认发送也有个最大值为100000
            if plan.data_num is None or plan.data_num < 0:
                plan.data_num = 100000

            # 每一批次1000条发送，发送太多了
            for i in range(plan.data_num // 1000):
                result_data_list = []
                for n in range(1000):
                    data_json = TaskExecutor._generate_data(TaskExecutor.tasks[task_id])
                    result_data_list.append(data_json)
                yield result_data_list
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
