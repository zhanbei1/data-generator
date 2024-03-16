#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> engine
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/2 13:31
@Desc   ：
==================================================
"""
import asyncio
import threading

from src.com_desmond.models.TaskModel import TaskModel, TaskExecutorPlan
from src.com_desmond.services.executor.TaskExecutor import TaskExecutor
from src.com_desmond.services.output import Output
from src.com_desmond.services.scheduler.TaskScheduler import TaskScheduler


class GeneratorCoreEngine:
    """
    数据生成器核心引擎, 负责所有任务调度，注册，等工作
    """
    tasks = {}

    @staticmethod
    def register_task(task_model: TaskModel):
        """
        注册任务
        :param task_model:
        :param task_id: 任务ID
        :param task_func: 任务函数
        :return:
        """
        print(f"register_task {task_model.name}")
        GeneratorCoreEngine.tasks[task_model.file_path] = task_model
        TaskExecutor.register_tasks(task_model.file_path, task_model.fields)
        TaskScheduler.register_scheduler(task_model.file_path, task_model.range_frequency)
        Output.register_output(task_model.file_path, task_model.output)

    @staticmethod
    def unregister_task(task_id: str):
        """
        取消注册任务
        :param task_id: 任务ID
        :return:
        """
        GeneratorCoreEngine.tasks.pop(task_id)
        TaskExecutor.unregister_task(task_id)
        TaskScheduler.unregister_task(task_id)
        Output.unregister_task(task_id)

    @staticmethod
    async def run_task():
        """
        运行任务
        :param task_id: 任务ID
        :return:
        """
        for task_plans in TaskScheduler.task_iterator():
            tasks = [GeneratorCoreEngine._generate_data_and_send(plan) for plan in task_plans]
            await asyncio.gather(*tasks)

    @staticmethod
    async def _generate_data_and_send(plan: TaskExecutorPlan):
        data_list = TaskExecutor.execute(plan.task_id, plan)
        Output.output(plan.task_id, data_list)


if __name__ == '__main__':
    engine = GeneratorCoreEngine()


    def task1():
        print("Task 1 is running")
