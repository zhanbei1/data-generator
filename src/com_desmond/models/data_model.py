#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> data_model
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/2 13:15
@Desc   ：数据生成模型
==================================================
"""
import math
import random
from datetime import datetime, timedelta

from src.com_desmond.exceptions.exceptions import TaskNotStartError, TaskRunCompletedError
from src.com_desmond.models.TaskModel import RangeFrequency


class BaseDataModel:
    """
    数据生成模型
    """

    def __init__(self, config: RangeFrequency):
        self.config = config

    def generate_data(self, timestamp: int) -> int:
        """
        生成数据
        :param timestamp: 生成数据的时间戳
        :return:
        """
        raise NotImplementedError("generate_data method must be implemented")

    def generate_log_count(self, base_count: int) -> int:
        # 抖动系数
        shake = self.config.data_distribution_config.shake
        # 最大最小值
        min_count = self.config.data_distribution_config.min_data_num
        max_count = self.config.data_distribution_config.max_data_num

        # 应用抖动参数
        base_count = int(base_count * (1 + shake * (random.random() - 0.5)))

        # 应用异常点
        for anomaly_config in self.config.data_anomaly:
            if random.random() < anomaly_config.ratio:
                base_count *= anomaly_config.magnification
                break  # 只应用一个异常点

        # 确保数量在最小值和最大值之间
        base_count = max(min_count, min(base_count, max_count))
        return base_count

    def check_task_status(self, timestamp: int):
        # 检查时间戳是否在时间范围内，如果结束时间为None，表示没有结束时间
        if self.config.end_timestamp is not None and timestamp > self.config.end_timestamp:
            raise TaskRunCompletedError("Timestamp is out of the given time range.")
        if timestamp < self.config.start_timestamp:
            raise TaskNotStartError("Timestamp is less of the given start time")


class PeriodicData(BaseDataModel):
    """
    周期性数据模型 PERIODIC_DATA
    """

    def __init__(self, config: RangeFrequency):
        super().__init__(config)
        self.config = config

    def generate_data(self, timestamp: int) -> int:
        self.check_task_status(timestamp)
        # 计算时间戳相对于开始时间的偏移量
        offset = timestamp - self.config.start_timestamp

        # 最大最小值
        min_count = self.config.data_distribution_config.min_data_num
        max_count = self.config.data_distribution_config.max_data_num

        # TODO: 假设周期为一天，可根据需要调整
        cycle_duration = timedelta(days=1).microseconds
        cycle_offset = offset % cycle_duration
        cycle_ratio = cycle_offset / cycle_duration
        base_count = int(min_count + (max_count - min_count) * math.sin(cycle_ratio * 2 * math.pi) * 0.5 + (
                max_count + min_count) * 0.5)

        return self.generate_log_count(base_count)


class LinearData(BaseDataModel):
    """
    一个简单的线性数据模型，用于生成线性数据。
    """

    def __init__(self, config: RangeFrequency):
        super().__init__(config)
        self.config = config

    def generate_data(self, timestamp: int):
        self.check_task_status(timestamp)
        # 计算时间戳相对于开始时间的偏移量
        if self.config.end_timestamp is not None:
            duration = self.config.end_timestamp - self.config.start_timestamp
        else:
            duration = 1

        offset = timestamp - self.config.start_timestamp
        offset_ratio = offset / duration
        # 最大最小值
        min_count = self.config.data_distribution_config.min_data_num
        max_count = self.config.data_distribution_config.max_data_num

        base_count = int(min_count + (max_count - min_count) * offset_ratio)
        return self.generate_log_count(base_count)


class RandomData(BaseDataModel):
    """
    一个简单的随机数据模型，用于生成随机数据。
    """

    def __init__(self, config: RangeFrequency):
        super().__init__(config)
        self.config = config

    def generate_data(self, timestamp: int):
        self.check_task_status(timestamp)
        # 最大最小值
        min_count = self.config.data_distribution_config.min_data_num
        max_count = self.config.data_distribution_config.max_data_num
        base_count = random.randint(min_count, max_count)
        return self.generate_log_count(base_count)


class AllOutData(BaseDataModel):
    """
    一个简单的全力输出模型，尽机器所具有的资源，不停的发送数据，不受任何参数限制
    """

    def __init__(self, config: RangeFrequency):
        super().__init__(config)
        self.config = config

    def generate_data(self, timestamp: int):
        self.check_task_status(timestamp)
        return -1
