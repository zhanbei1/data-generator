#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> test_tasks_config_file_scan
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/2/29 13:54
@Desc   ：
==================================================
"""
import asyncio
import os

from src.com_desmond.models.TaskModel import TaskModel
from src.com_desmond.services.config_parsers.ConfigParser import ConfigParser
from src.com_desmond.services.engine.engine import GeneratorCoreEngine
from src.com_desmond.services.tasks_config_file_scan import FileChangeHandler, handle_file_change
import time
from watchdog.observers import Observer


def test_handle_file_change():
    # 指定要监控的目录
    directory_to_watch = '/Users/zhanbei/PycharmProjects/data-generator/tasks_running/'

    for root, dirs, files in os.walk(directory_to_watch):
        for file in files:
            file_path = os.path.join(root, file)
            task: TaskModel = ConfigParser.analysis_by_file_path(file_path)
            GeneratorCoreEngine.register_task(task)
    asyncio.run(GeneratorCoreEngine.run_task())

    event_handler = FileChangeHandler(handle_file_change())
    observer = Observer()
    observer.schedule(event_handler, path=directory_to_watch, recursive=True)

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
    assert True


def read_all_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"文件路径: {file_path}")
                print(f"文件内容:\n{content}\n")
