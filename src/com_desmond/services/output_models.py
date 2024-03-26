#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> output_models
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/7 14:37
@Desc   ：输出的数据源
==================================================
"""
import multiprocessing
import time
from asyncio import Queue
from multiprocessing import Pool

from typing import List

import ujson
from pydantic import BaseModel

from src.com_desmond.models.TaskModel import KafkaOutputConfig, FileOutputConfig


class BaseOutputModel:
    """
    基础输出模型
    """

    def close(self):
        raise NotImplementedError("notImplementedError")

    def check_config(self, config: BaseModel):
        raise NotImplementedError("notImplementedError")

    def send_data(self, data: dict):
        raise NotImplementedError("notImplementedError")

    def send_data_list(self, data_list: List[str | dict]):
        for data in data_list:
            self.send_data(data)


class KafkaOutputModel(BaseOutputModel):

    def __init__(self, output_config: KafkaOutputConfig):
        print(f"KafkaOutputModel init {output_config}")
        self.check_config(output_config)
        self.extra_config: dict = output_config.extra_config
        self.extra_config["bootstrap.servers"] = output_config.kafka_address
        self.async_queue = multiprocessing.Manager().Queue(-1)
        self.producer_pool = Pool(processes=1)
        self.producer_pool.apply_async(func=_async_send_data,
                                       args=(self.async_queue, output_config.kafka_topic, self.extra_config),
                                       error_callback=_error_callback)
        self.producer_pool.close()
        # self.producer_pool.join()

    def close(self):
        self.producer_pool.terminate()

    def check_config(self, config: KafkaOutputConfig):
        if config.kafka_address is None or config.kafka_topic is None:
            raise ValueError("kafka_address or kafka_topic is None")

    def send_data(self, data):
        if type(data) is dict:
            data_str = ujson.dumps(data)
        else:
            data_str = data
        # print(f"KafkaOutputModel send_data {data}")
        self.async_queue.put(data_str, True, 1)


def _async_send_data(queue, topic: str, extra_config: dict):
    from confluent_kafka.cimpl import Producer
    producer = Producer(**extra_config)
    try:
        while True:
            try:
                data = queue.get(True, 1)
                # print(f"KafkaOutputModel _async_send_data {data}")
                producer.produce(topic, data)
                producer.flush(1)
            except Exception as e:
                print(f"Queue get Empty exception time.sleep(1), e:{e}")
                time.sleep(1)
    except KeyboardInterrupt as e:
        print(e)
    finally:
        producer.flush(1)


def _error_callback(err):
    print(f"KafkaOutputModel processor pool 错误异常 ： {str(err)}")


class FileOutputModel(BaseOutputModel):
    def __init__(self, output_config: FileOutputConfig):
        pass

    def close(self):
        pass

    def check_config(self, config: BaseModel):
        pass

    def send_data(self, data: dict):
        pass
