#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> utils
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/21 23:53
@Desc   ：
==================================================
"""
import ujson

from database.sqllite3 import Task
from src.com_desmond.enums.TaskPlanStatus import TaskPlanStatus
from src.com_desmond.models.TaskModel import TaskModel, RangeFrequency, FiledConfig, OutputConfig


def db_task_to_model(task: Task) -> TaskModel:
    task_model = TaskModel(
        name=task.name,
        id=task.id,
        task_status=TaskPlanStatus[task.task_status].value,
        description=task.description,
        range_frequency=RangeFrequency.model_validate(ujson.loads(task.range_frequency)),
        output=OutputConfig.model_validate(ujson.loads(task.output)),
        fields=[FiledConfig.model_validate(ujson.loads(filed)) for filed in ujson.loads(task.fields)]
    )
    return task_model


def model_to_db_task(task: TaskModel) -> Task:
    db_task = Task()
    db_task.name = task.name if task.name is not None else db_task.name
    db_task.task_status = task.task_status if task.task_status is not None else db_task.task_status
    db_task.description = task.description if task.description is not None else db_task.description
    db_task.range_frequency = ujson.dumps(
        task.range_frequency.json()) if task.range_frequency is not None else db_task.range_frequency
    db_task.fields = ujson.dumps(task.fields.json()) if task.fields is not None else db_task.fields
    db_task.output = ujson.dumps(task.output.json()) if task.output is not None else db_task.output
    return db_task
