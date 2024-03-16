#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> tasks_config_file_scan
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/2/29 11:46
@Desc   ：任务配置文件夹内的任务文件扫描
==================================================
"""

from watchdog.events import FileSystemEventHandler, FileSystemEvent

from src.com_desmond.models.TaskModel import TaskModel
from src.com_desmond.services.config_parsers.ConfigParser import ConfigParser
from src.com_desmond.services.engine.engine import GeneratorCoreEngine


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, action_on_change):
        self.action_on_change = action_on_change

    def on_created(self, event: FileSystemEvent) -> None:
        self.execute_action(event)

    def on_modified(self, event):
        self.execute_action(event)

    def on_deleted(self, event: FileSystemEvent) -> None:
        self.execute_action(event)

    def on_created(self, event: FileSystemEvent) -> None:
        self.execute_action(event)

    def on_moved(self, event: FileSystemEvent) -> None:
        self.execute_action(event)

    def execute_action(self, event: FileSystemEvent):
        if not event.is_directory and event.src_path.endswith(('.txt', '.json', '.csv', '.py')):  # 自定义监控的文件扩展名
            print(f"文件 {event.src_path} 已被修改！")
            self.action_on_change(event)


# EVENT_TYPE_MOVED = "moved"
# EVENT_TYPE_DELETED = "deleted"
# EVENT_TYPE_CREATED = "created"
# EVENT_TYPE_MODIFIED = "modified"
# EVENT_TYPE_CLOSED = "closed"
# EVENT_TYPE_OPENED = "opened"

def handle_file_change():
    def inner_action(event: FileSystemEvent):
        if event.event_type in ("moved", "deleted"):
            GeneratorCoreEngine.unregister_task(event.src_path)
        elif event.event_type in ("created", "modified"):
            task: TaskModel = ConfigParser.analysis_by_file_path(event.src_path)
            GeneratorCoreEngine.register_task(task)

    return inner_action
