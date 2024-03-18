#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> TaskModel
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/2/29 19:37
@Desc   ：执行生成数据的任务模型
==================================================
"""
import time
from typing import List, Tuple

from pydantic import BaseModel, Field

from src.com_desmond.enums.TaskPlanStatus import TaskPlanStatus
from src.com_desmond.enums.output_type_enum import OutputTypeEnum


class DataAnomaly(BaseModel):
    """
    数据异常配置
    """
    # 异常数据概率
    ratio: float = Field(default=0.01, ge=0, le=1)
    # 异常数据倍率
    magnification: int = Field(default=1)


class DataDistributionConfig(BaseModel):
    range: int = Field(default=0, description="变化周期时间, 仅仅用于周期变化模型, 样例：6d, 7h等")
    max_data_num: int = Field(default=1000000, description="变化周期内的最大值")
    min_data_num: int = Field(default=0, description="变化周期内的最小值")
    shake: float = Field(default=0.01, ge=0, le=1, description="抖动值")


class RangeFrequency(BaseModel):
    """
     生成数据的时间频率
     """
    # 时间范围【startTimestamp, endTimestamp】
    start_timestamp: int = Field(default=int(time.time() * 1000), description="开始时间戳")
    end_timestamp: int = Field(default=None, description="结束时间戳")
    # 数据模型分布类型
    data_distribution: str = Field(default="ALL_OUT_DATA")
    # 数据分布模型配置
    data_distribution_config: DataDistributionConfig = Field(default=None)
    # 数据异常分布模型
    data_anomaly: List[DataAnomaly] = Field(default=[])


class FiledConfig(BaseModel):
    """
    数据模型字段
    """
    # 字段名称
    name: str
    # 字段类型
    data_type: str
    # 字段类型的其他额外配置
    extra_config: dict


class FileOutputConfig(BaseModel):
    """
    文件类型存储配置
    """
    # 输出数据存储位置
    file_path: str


class KafkaOutputConfig(BaseModel):
    """
    kafka类型存储配置
    """
    # kafka地址
    kafka_address: str
    # kafka topic
    kafka_topic: str
    # kafka 的其他配置
    extra_config: dict


class OutputConfig(BaseModel):
    """
    数据模型输出配置
    """
    output_type: OutputTypeEnum = Field(default=OutputTypeEnum.KAFKA.name)
    # 文件类型存储配置
    file_output: FileOutputConfig = Field(default=None)
    # 输出数据存储位置
    kafka_output: KafkaOutputConfig = Field(default=None)


class TaskModel(BaseModel):
    """
    执行生成数据的任务模型
    """
    name: str
    file_path: str = Field(default="")
    id: str = Field(default="")
    description: str
    range_frequency: RangeFrequency
    fields: List[FiledConfig]
    output: OutputConfig


class TaskExecutorPlan(BaseModel):
    # 任务状态
    task_status: TaskPlanStatus = Field(default=TaskPlanStatus.IN_PROGRESS)
    # 任务ID
    task_id: str = Field(default="")
    # 开始时间
    start_timestamp: int = Field(default=int(time.time() * 1000))
    # 结束时间
    end_timestamp: int = Field(default=int(time.time() * 1000))
    # 数据产生个数
    data_num: int = Field(default=1000)
