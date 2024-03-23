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

from config.basic_config import logger
from src.com_desmond.enums.TaskPlanStatus import TaskPlanStatus
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
        try:
            task_model.task_status = TaskPlanStatus.IN_PROGRESS
            GeneratorCoreEngine.tasks[task_model.id] = task_model
            TaskExecutor.register_tasks(task_model.id, task_model.fields)
            TaskScheduler.register_scheduler(task_model.id, task_model.range_frequency)
            Output.register_output(task_model.id, task_model.output)
        except Exception as e:
            GeneratorCoreEngine.unregister_task(task_model.id)
            raise RuntimeError("GeneratorCoreEngine register_task error ,rollback。error info ", e)

    @staticmethod
    def unregister_task(task_id: str):
        """
        取消注册任务
        :param task_id: 任务ID
        :return:
        """
        try:
            GeneratorCoreEngine.tasks.pop(task_id)
            TaskExecutor.unregister_task(task_id)
            TaskScheduler.unregister_task(task_id)
            Output.unregister_task(task_id)
        except Exception as e:
            print(f"Engine unregister_task error  :{e}")

    @staticmethod
    async def run_task():
        """
        运行任务
        :param task_id: 任务ID
        :return:
        """
        for task_plans in TaskScheduler.task_iterator():
            tasks = []
            for plan in task_plans:
                plan: TaskExecutorPlan
                # 任务停止或者被打断，则移除任务队列
                if plan.task_status in (TaskPlanStatus.COMPLETED, TaskPlanStatus.TERMINATED):
                    logger.info(f"Task {plan.task_id} is terminated or completed, remove it from task queue,")
                    print(f"Task {plan.task_id} is terminated or completed, remove it from task queue,")
                    GeneratorCoreEngine.unregister_task(plan.task_id)
                elif plan.task_status == TaskPlanStatus.NOT_STARTED:  # 还没有开始，则不运行
                    logger.info(f"Task {plan.task_id} is not started,skip it.")
                    print(f"Task {plan.task_id} is not started,skip it.")
                    continue
                elif plan.task_status == TaskPlanStatus.IN_PROGRESS:
                    tasks.append(GeneratorCoreEngine._generate_data_and_send(plan))
            await asyncio.gather(*tasks)

    @staticmethod
    async def _generate_data_and_send(plan: TaskExecutorPlan):
        try:
            for data_list in TaskExecutor.execute(plan.task_id, plan):
                Output.output(plan.task_id, data_list)
        except Exception as e:
            logger.error("GeneratorCoreEngine _generate_data_and_send error , error info : ", e)
