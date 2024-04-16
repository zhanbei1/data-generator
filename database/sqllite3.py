#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> sqllite3
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/21 22:30
@Desc   ：
==================================================
"""

from sqlalchemy import create_engine, Column, String, DateTime, func, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time


def current_timestamp_millis():
    timestamp = time.time()
    timestamp_millis = int(timestamp * 1000)
    return timestamp_millis


engine = create_engine('sqlite:///database/tasks.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# 定义基础类
Base = declarative_base()


# 定义任务模型
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(String, primary_key=True, comment="任务唯一ID，UUID")
    name = Column(String, comment='任务名称')
    task_status = Column(String, comment='任务状态,'
                                         'NOT_STARTED:计划中,'
                                         'IN_PROGRESS:运行中,'
                                         'COMPLETED:已完成,'
                                         'FAILED：失败 ')
    description = Column(String, comment="任务描述")
    range_frequency = Column(String, comment="任务频率, JSON 字符串")
    fields = Column(String, comment="任务字段, JSON 字符串")
    output = Column(String, comment="任务输出, JSON 字符串")
    create_time = Column(DateTime, comment="任务创建时间", default=func.now())
    update_time = Column(DateTime, comment="任务更新时间", default=func.now(), onupdate=func.now())


# 定义字段模版
class FieldTemplate(Base):
    __tablename__ = 'field_templates'
    id = Column(String, primary_key=True, comment="字段模版唯一ID，UUID")
    name = Column(String, comment='字段模版名称')
    description = Column(String, comment="字段模版描述")
    field_config = Column(String, comment="字段模版字段, JSON 字符串")
    create_time = Column(Integer, comment="字段模版创建时间，毫秒时间戳", default=current_timestamp_millis)
    update_time = Column(Integer, comment="字段模版更新时间", default=current_timestamp_millis,
                         onupdate=current_timestamp_millis)


# 创建表（如果表不存在）
Base.metadata.create_all(engine)
