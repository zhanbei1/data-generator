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

from database.sqllite3 import Task, FieldTemplate
from src.com_desmond.enums.TaskPlanStatus import TaskPlanStatus
from src.com_desmond.models.TaskModel import TaskModel, RangeFrequency, FieldConfig, OutputConfig
from vo.vo import FieldTemplateVO


def db_task_to_model(task: Task) -> TaskModel:
    task_model = TaskModel(
        name=task.name,
        id=task.id,
        task_status=TaskPlanStatus[task.task_status].value,
        description=task.description,
        range_frequency=RangeFrequency.model_validate(ujson.loads(task.range_frequency)),
        output=OutputConfig.model_validate(ujson.loads(task.output)),
        fields=[FieldConfig.model_validate(ujson.loads(field)) for field in ujson.loads(task.fields)]
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


def model_to_db_field_template(field: FieldTemplateVO) -> FieldTemplate:
    db_field_template = FieldTemplate()
    db_field_template.id = field.id if field.id is not None else None
    db_field_template.name = field.name if field.name is not None else db_field_template.name
    db_field_template.description = field.description if field.description is not None else db_field_template.description
    fields_config_json = [k.dict() for k in
                          field.field_config] if field.field_config is not None else db_field_template.field_config
    db_field_template.field_config = ujson.dumps(fields_config_json)
    return db_field_template


def db_field_template_to_model(db_field_template: FieldTemplate) -> FieldTemplateVO:
    field = FieldTemplateVO()
    field.id = db_field_template.id if db_field_template.id is not None else field.id
    field.name = db_field_template.name if db_field_template.name is not None else field.name
    field.description = db_field_template.description if db_field_template.description is not None else field.description
    field.update_time = db_field_template.update_time
    field.create_time = db_field_template.create_time
    if db_field_template.field_config is not None:
        field.field_config = [FieldConfig.parse_obj(k) for k in ujson.loads(db_field_template.field_config)]
    return field

