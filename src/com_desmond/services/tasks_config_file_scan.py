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


class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, action_on_change):
        self.action_on_change = action_on_change

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(('.txt', '.json', '.csv', '.py')):  # 自定义监控的文件扩展名
            print(f"文件 {event.src_path} 已被修改！")
            self.action_on_change(event.src_path)

    def on_deleted(self, event: FileSystemEvent) -> None:
        pass

    def on_created(self, event: FileSystemEvent) -> None:
        pass

    def on_moved(self, event: FileSystemEvent) -> None:
        pass


def handle_file_change():
    def inner_action(file_path: str):
        print(f"重新读取文件 {file_path} 的内容：")
        with open(file_path, 'r') as modified_file:
            content = modified_file.read()
            print(content)

    return inner_action
