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
import multiprocessing

from src.com_desmond.node import Node
from src.com_desmond.services.engine.engine import GeneratorCoreEngine

if __name__ == '__main__':
    process_list = []
    node = Node()
    # 发送心跳
    heart_process = multiprocessing.Process(target=node.send_heartbeat)
    heart_process.start()
    process_list.append(heart_process)

    # 接受master任务
    receive_process = multiprocessing.Process(target=node.receive_messages)
    receive_process.start()
    process_list.append(receive_process)
    # 等待进程结束（如果你不想程序立即退出，可以注释掉这行代码）
    for p in process_list:
        p.join()

    # 创建一个Process对象，target指向要运行的函数
    asyncio.run(GeneratorCoreEngine.run_task())

    for p in process_list:
        p.close()
    node.close()

    # 指定要监控的目录
    # directory_to_watch = "../../" + GlobalBaseConfig.task_running_dir
    #
    # for root, dirs, files in os.walk(directory_to_watch):
    #     for file in files:
    #         file_path = os.path.join(root, file)
    #         task: TaskModel = ConfigParser.analysis_by_file_path(file_path)
    #         GeneratorCoreEngine.register_task(task)
    # asyncio.run(GeneratorCoreEngine.run_task())
    #
    # event_handler = FileChangeHandler(handle_file_change())
    # observer = Observer()
    # observer.schedule(event_handler, path=directory_to_watch, recursive=True)
    #
    # observer.start()
    #
    # try:
    #     while True:
    #         time.sleep(5)
    # except KeyboardInterrupt:
    #     observer.stop()
    #
    # observer.join()
