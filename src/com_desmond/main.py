#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> main
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/13 10:36
@Desc   ：
==================================================
"""
import asyncio
import os
import time

from src.com_desmond.models.TaskModel import TaskModel
from src.com_desmond.services.config_parsers.ConfigParser import ConfigParser
from src.com_desmond.services.engine.engine import GeneratorCoreEngine
from src.com_desmond.services.tasks_config_file_scan import FileChangeHandler, handle_file_change
from watchdog.observers import Observer

if __name__ == '__main__':
    # 指定要监控的目录
    directory_to_watch = 'tasks_running/'

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
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()