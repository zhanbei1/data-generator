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
from master_node import MasterNode
from src.com_desmond.enums.DataTypeEnum import DataTypeEnum, DataType
from src.com_desmond.enums.TaskPlanStatus import TaskPlanStatus
from src.com_desmond.models.TaskModel import TaskModel
from utils import db_task_to_model
from sqlalchemy import event
from sqlalchemy.sql import desc
from vo.vo import DataTypeVo

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})
# 设置静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 使用Jinja2作为模板引擎
env = Environment(loader=FileSystemLoader('static/html_json_config'))  # 假设你的模板文件在'templates'文件夹中

html_template_path = "index.html"
html_view_json = "static/html_json_config/task_view.json"

# master节点
master_node = MasterNode()
master_node.start_listening()


@event.listens_for(session, 'before_flush')
def receive_before_flush(session: Session, flush_context, instances):
    # listen for the 'before_flush' event
    original_values = []
    # 记录新增的对
    for obj in session.new:
        original_values.append(obj)
    # 记录被删除的对象及其原始值
    for obj in session.deleted:
        original_values.append(obj)
    # 记录被修改的对象及其原始值
    for obj in session.dirty:
        # original_state = session.identity_map.get_state(obj)  # 获取原始状态
        # if ('task_status' in original_state.dict and original_state.dict['task_status'] != obj.task_status) \
        #         or ('range_frequency' in original_state.dict and original_state.dict[
        #     'range_frequency'] != obj.range_frequency) \
        #         or ('fields' in original_state.dict and original_state.dict['fields'] != obj.fields) \
        #         or ('output' in original_state.dict and original_state.dict['output'] != obj.fields):
        # my_field 字段发生了变化
        # 在这里发送通知
        original_values.append(obj)

    if original_values is not None:
        slave_task = []
        for v in original_values:
            task_model = db_task_to_model(v)
            slave_task.append(task_model.json())

        # 通知
        master_node.broadcast_message(ujson.dumps(slave_task))


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
        db_task.task_status = TaskPlanStatus.NOT_STARTED.name
        db.commit()
    return JSONResponse(content={"message": "Task deleted successfully"}, status_code=200)


@app.get("/task-list", response_model=List[TaskModel])
async def task_list(db: Session = Depends(get_db)):
    tasks: List[Task] = db.query(Task).order_by(desc(Task.update_time)).all()
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


@app.get("/node-list")
async def node_list(request: Request):
    nodes: dict = master_node.nodes
    node_address_list = [{"ip": v.ip, "port": v.port, "status": "pending"} for k, v in nodes.items()]
    return JSONResponse(content=node_address_list, status_code=200)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

    # 关闭所有资源
    master_node.close()
    session.close()
    print("API stop =======> ")
