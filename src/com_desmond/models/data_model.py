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
from src.com_desmond.models.TaskModel import DataDistributionConfig


class BaseDataModel:
    """
    数据生成模型
    """

    def __init__(self, config: DataDistributionConfig):
        self.config = config

    def generate_data(self) -> int:
        raise NotImplementedError("generate_data method must be implemented")


class PeriodicData(BaseDataModel):
    """
    周期性数据模型
    """

    def __init__(self, config: DataDistributionConfig):
        super().__init__(config)
        self.config = config

    def generate_data(self) -> int:
        # TODO : 默认-1 为不限制
        return -1

    def inject_outliers(self, data):
        # 示例：在数据中每间隔一定数量的点添加一个异常值
        outlier_points = np.where(np.random.rand(len(data)) < 0.1)[0]
        for point in outlier_points:
            data[point] = self.outlier_func(data[point])
        return data


class LinearData(BaseDataModel):
    """
    一个简单的线性数据模型，用于生成线性数据。
    """

    def __init__(self, config: DataDistributionConfig):
        super().__init__(config)
        self.config = config

    def generate_data(self):
        pass


class SineData(BaseDataModel):
    """
    一个简单的正弦数据模型，用于生成正弦数据。
    """

    def __init__(self, config: DataDistributionConfig):
        super().__init__(config)
        self.config = config

    def generate_data(self):
        pass


class RandomData(BaseDataModel):
    """
    一个简单的随机数据模型，用于生成随机数据。
    """

    def __init__(self, config: DataDistributionConfig):
        super().__init__(config)
        self.config = config

    def generate_data(self):
        pass


class AllOutData(BaseDataModel):
    """
    一个简单的全力输出模型，尽机器所具有的资源，不停的发送数据，不受任何参数限制
    """

    def __init__(self, config: DataDistributionConfig):
        super().__init__(config)
        self.config = config

    def generate_data(self):
        return -1
