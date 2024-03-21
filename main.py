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
import uuid
from typing import List

import ujson
from fastapi import FastAPI, Request, Body, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from jinja2 import Environment, FileSystemLoader

from config.basic_config import GlobalBaseConfig
from database.sqllite3 import Session, Task, session
from src.com_desmond.enums.DataTypeEnum import DataTypeEnum, DataType
from src.com_desmond.enums.TaskPlanStatus import TaskPlanStatus
from src.com_desmond.models.TaskModel import TaskModel
from utils import db_task_to_model
from vo.vo import DataTypeVo

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})
# 设置静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 使用Jinja2作为模板引擎
env = Environment(loader=FileSystemLoader('static/html_json_config'))  # 假设你的模板文件在'templates'文件夹中

html_template_path = "index.html"
html_view_json = "static/html_json_config/task_view.json"


# 依赖项，用于数据库会话管理
def get_db():
    try:
        db = session
        yield db
    finally:
        db.close()


@app.get("/")
async def read_root(request: Request):
    # 渲染模板，并将AMIS JSON传递给模板
    template = env.get_template(html_template_path)
    with open(html_view_json, "r", encoding="utf-8") as f:
        html_content = template.render(amis_json=f.read())
        return HTMLResponse(content=html_content, status_code=200)


@app.post("/create-task")
async def create_task(task_config: TaskModel = Body(...), db: Session = Depends(get_db)):
    task_config.id = str(uuid.uuid4())
    task = Task(id=task_config.id, name=task_config.name, task_status=TaskPlanStatus.NOT_STARTED.name,
                description=task_config.description,
                range_frequency=task_config.range_frequency.json(),
                fields=ujson.dumps([field.json() for field in task_config.fields]),
                output=task_config.output.json()
                )
    db.add(task)
    db.commit()
    db.refresh(task)
    return JSONResponse(content={"message": "Save success"}, status_code=200)


@app.put("/update-task/{task_id}/")
async def update_task(task_id: str, task: TaskModel, db: Session = Depends(get_db)):
    db_task: Task = db.query(Task).get(task_id)
    if not db_task:
        return JSONResponse(content={"message": "Task not found"}, status_code=200)
    db_task.name = task.name if task.name is not None else db_task.name
    db_task.task_status = task.task_status if task.task_status is not None else db_task.task_status
    db_task.description = task.description if task.description is not None else db_task.description
    db_task.range_frequency = ujson.dumps(
        task.range_frequency.json()) if task.range_frequency is not None else db_task.range_frequency
    db_task.fields = ujson.dumps(task.fields.json()) if task.fields is not None else db_task.fields
    db_task.output = ujson.dumps(task.output.json()) if task.output is not None else db_task.output
    db.commit()

    return JSONResponse(content={"message": "Task updated successfully"}, status_code=200)


@app.post("/batch-delete")
async def batch_delete(delete_info: dict, db: Session = Depends(get_db)):
    tasks_id = delete_info.get("tasks_id", [])
    for task_id in tasks_id:
        db_task = db.query(Task).get(task_id)
        if db_task:
            db.delete(db_task)
            db.commit()
    return JSONResponse(content={"message": "Task deleted successfully"}, status_code=200)


@app.post("/delete-task")
async def batch_delete(delete_info: dict, db: Session = Depends(get_db)):
    task_id = delete_info.get("task_id", None)
    if not task_id:
        return JSONResponse(content={"message": "Task id is required"}, status_code=400)
    db_task = db.query(Task).get(task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
    return JSONResponse(content={"message": "Task deleted successfully"}, status_code=200)


@app.post("/enable-task")
async def enable_task(request_dict: dict, db: Session = Depends(get_db)):
    task_id = request_dict.get("task_id", None)
    if not task_id:
        return JSONResponse(content={"message": "Task id is required"}, status_code=400)

    db_task: Task = db.query(Task).get(task_id)
    if db_task:
        db_task.task_status = TaskPlanStatus.IN_PROGRESS.name
        db.commit()
    return JSONResponse(content={"message": "Task deleted successfully"}, status_code=200)


@app.post("/disable-task")
async def disable_task(request_dict: dict, db: Session = Depends(get_db)):
    task_id = request_dict.get("task_id", None)
    if not task_id:
        return JSONResponse(content={"message": "Task id is required"}, status_code=400)

    db_task: Task = db.query(Task).get(task_id)
    if db_task:
        db_task.task_status = TaskPlanStatus.NOT_STARTED.value
        db.commit()
    return JSONResponse(content={"message": "Task deleted successfully"}, status_code=200)


@app.get("/task-list", response_model=List[TaskModel])
async def task_list(db: Session = Depends(get_db)):
    tasks: List[Task] = db.query(Task).all()
    task_array: list[TaskModel] = []
    for task in tasks:
        task_array.append(db_task_to_model(task))
    return task_array


@app.get("/task-detail/{task_id}", response_model=TaskModel)
async def task_list(task_id: str, db: Session = Depends(get_db)):
    task_db = db.query(Task).filter(Task.id == task_id).first()
    if not task_db:
        return JSONResponse(content={"message": "Task not found"}, status_code=200)
    return TaskModel.from_orm(task_db)


@app.get("/data-type-list")
async def data_type_list(request: Request):
    type_list = []
    for name in dir(DataTypeEnum):
        if not name.startswith('__'):
            data_type: DataType = DataTypeEnum.value_of(name)
            type_vo = DataTypeVo(name=name, type=data_type.name, description=data_type.description,
                                 sample=data_type.sample)
            type_list.append(ujson.loads(type_vo.json()))
    return JSONResponse(content=type_list, status_code=200)


@app.get("/helper-file")
async def helper_file(file_name: str = Body(...)):
    file_path = os.path.join(GlobalBaseConfig.helper_file_dir, file_name)
    if os.path.exists(file_path):
        return FileResponse(file_path)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
