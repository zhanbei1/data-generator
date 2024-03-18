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
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse, JSONResponse
from jinja2 import Environment, FileSystemLoader

from config.basic_config import GlobalBaseConfig
from src.com_desmond.enums.TaskPlanStatus import TaskPlanStatus
from src.com_desmond.models.TaskModel import TaskModel
from src.com_desmond.services.config_parsers.ConfigParser import ConfigParser
from src.com_desmond.services.engine.engine import GeneratorCoreEngine

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
async def read_root(task_config: TaskModel = Body(...)):
    file_path = task_repository + "/" + task_config.name + ".json"
    running_task_path = task_running + "/" + task_config.name + ".json"
    if pathlib.Path(file_path).exists() or pathlib.Path(running_task_path).exists():
        return JSONResponse(content="Same task already exists", status_code=501)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(task_config.json())
    return JSONResponse(content="Save success", status_code=200)


@app.post("/delete-task")
async def read_root(task_path: str = Body(...)):
    if pathlib.Path(task_path).exists():
        os.remove(task_path)
    return JSONResponse(content="Save success", status_code=200)


@app.get("/task-list")
async def read_root(request: Request):
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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
