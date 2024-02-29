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
from src.com_desmond.services.tasks_config_file_scan import FileChangeHandler, handle_file_change
import time
from watchdog.observers import Observer


def test_handle_file_change():
    # 指定要监控的目录
    directory_to_watch = '/path/to/your/directory'

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
