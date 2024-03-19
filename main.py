#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：data-generator -> main
@IDE    ：PyCharm
@Author ：Desmond.zhan
@Date   ：2024/3/18 10:16
@Desc   ：
==================================================
"""
import os
import pathlib

import ujson
from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from jinja2 import Environment, FileSystemLoader

from config.basic_config import GlobalBaseConfig
from src.com_desmond.enums.DataTypeEnum import DataTypeEnum, DataType
from src.com_desmond.enums.TaskPlanStatus import TaskPlanStatus
from src.com_desmond.models.TaskModel import TaskModel
from src.com_desmond.services.config_parsers.ConfigParser import ConfigParser
from src.com_desmond.services.engine.engine import GeneratorCoreEngine
from vo.vo import DataTypeVo

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

# 使用Jinja2作为模板引擎
env = Environment(loader=FileSystemLoader('html_json_config'))  # 假设你的模板文件在'templates'文件夹中

html_template_path = "index.html"
html_view_json = "html_json_config/task_view.json"
task_repository = "task_repository"
task_running = "tasks_running"


@app.get("/")
async def read_root(request: Request):
    # 渲染模板，并将AMIS JSON传递给模板
    template = env.get_template(html_template_path)
    with open(html_view_json, "r", encoding="utf-8") as f:
        html_content = template.render(amis_json=f.read())
        return HTMLResponse(content=html_content, status_code=200)


@app.post("/create-task")
async def create_task(task_config: TaskModel = Body(...)):
    file_path = os.path.join(GlobalBaseConfig.task_repository, task_config.name + ".json")
    running_task_path = os.path.join(GlobalBaseConfig.task_running_dir, task_config.name + ".json")

    if pathlib.Path(file_path).exists() or pathlib.Path(running_task_path).exists():
        return JSONResponse(content="Same task already exists", status_code=501)
    else:
        task_config.task_status = TaskPlanStatus.NOT_STARTED
        with open(file_path, "x", encoding="utf-8") as f:
            f.write(str(task_config.json()))
        return JSONResponse(content={"message": "Save success"}, status_code=200)


@app.post("/delete-task")
async def delete_task(task_path: str = Body(...)):
    if pathlib.Path(task_path).exists():
        os.remove(task_path)
    return JSONResponse(content={"message": "Delete success"}, status_code=200)


@app.get("/task-list")
async def task_list(request: Request):
    task_running_dir = GlobalBaseConfig.task_running_dir
    task_repository_dir = GlobalBaseConfig.task_repository

    task_json_dict = {}

    task_list: list[TaskModel] = GeneratorCoreEngine.tasks.values()
    # 运行中的
    for task in task_list:
        task_json_dict[task.id] = task.json()

    # 在运行目录中，但是未运行的
    for root, dirs, files in os.walk(task_running_dir):
        for file in files:
            file_path = os.path.join(root, file)
            task: TaskModel = ConfigParser.analysis_by_file_path(file_path)
            task.task_status = TaskPlanStatus.TERMINATED
            task_json_dict[task.id] = task.json()
    # 未在运行目录中的
    for root, dirs, files in os.walk(task_repository_dir):
        for file in files:
            file_path = os.path.join(root, file)
            task: TaskModel = ConfigParser.analysis_by_file_path(file_path)
            task.task_status = TaskPlanStatus.NOT_STARTED
            task_json_dict[task.id] = task.json()

    return JSONResponse(content=[ujson.loads(task_json) for task_json in task_json_dict.values()], status_code=200)


@app.get("/data-type-list")
async def data_type_list(request: Request):
    type_list = []
    for name in dir(DataTypeEnum):
        if not name.startswith('__'):
            data_type: DataType = DataTypeEnum.value_of(name)
            type_vo = DataTypeVo(name=name, type=data_type.name)
            type_list.append(ujson.loads(type_vo.json()))
    return JSONResponse(content=type_list, status_code=200)


@app.get("/helper-file")
async def data_type_list(file_name: str = Body(...)):
    file_path = os.path.join(GlobalBaseConfig.helper_file_dir, file_name)
    if os.path.exists(file_path):
        return FileResponse(file_path)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
