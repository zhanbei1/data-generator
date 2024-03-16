#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> TaskScheduler
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/2 00:23
@Desc   ：任务调度器，根据模型和时间，生成一个个要执行的任务，每秒要执行的任务，任务执行周期最小秒级
==================================================
"""
import threading
import time
from typing import List

from src.com_desmond.enums.TaskPlanStatus import TaskPlanStatus
from src.com_desmond.models.TaskModel import RangeFrequency, TaskExecutorPlan


class TaskScheduler:
    tasks = {}

    @staticmethod
    def register_scheduler(task_id: str, range_frequency: RangeFrequency):
        """
        注册任务调度器，
        :return:
        """
        print(f"TaskScheduler register_task {task_id}")
        # TODO: 注册的应该是这个task——id对应的函数模型，后面可以根据这个函数模型直接生成对应的value
        # distribution_type = range_frequency.data_distribution
        # data_model: BaseDataModel = DataDistributionEnum.getDataModelByKey(distribution_type,
        #                                                                    frequency_task.data_distribution_config)
        # TaskScheduler.tasks[task_id] = data_model
        TaskScheduler.tasks[task_id] = range_frequency

    @staticmethod
    def unregister_task(task_id: str):
        TaskScheduler.tasks.pop(task_id)

    @staticmethod
    def log_curve(task_id: str, start_timestamp: int) -> TaskExecutorPlan:
        """
        TODO:根据模型和当前时间获取当前执行任务数量,已经执行完毕的任务，返回状态为finished，否则为continuing
        :param task_id:
        :param start_timestamp:
        :return:
        """
        if TaskScheduler.tasks[task_id] is not None:
            frequency_task: RangeFrequency = TaskScheduler.tasks[task_id]
            # distribution_type = frequency_task.data_distribution
            # data_model: BaseDataModel = DataDistributionEnum.getDataModelByKey(distribution_type,
            #                                                                    frequency_task.data_distribution_config)
            plan = TaskExecutorPlan()
            plan.task_status = TaskPlanStatus.IN_PROGRESS
            plan.task_id = task_id
            plan.start_timestamp = start_timestamp
            plan.end_timestamp = start_timestamp + 1000
            plan.data_num = frequency_task.data_distribution_config.max_data_num
            plan.anomaly = 0.1
            plan.ratio = 0.4
            return plan

    @staticmethod
    def generate_task(start_timestamp: int):
        """
        根据任务配置生成一个任务，并注册到tasks内
        :param start_timestamp:
        :param task:
        :return:
        """
        task_plan_list = []
        for task_id, task in TaskScheduler.tasks.items():
            task_plan_list.append(TaskScheduler.log_curve(task_id, start_timestamp))
        return task_plan_list

    @staticmethod
    def task_iterator() -> List[TaskExecutorPlan]:
        """
        每秒要执行的任务迭代器
        :return:
        """
        while threading.current_thread().is_alive():
            concurrent_timestamp = int(time.time() * 1000)
            yield TaskScheduler.generate_task(concurrent_timestamp)
            time.sleep(1)
