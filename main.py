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
import json
from pathlib import Path

import ujson
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

app = FastAPI()

# 使用Jinja2作为模板引擎
env = Environment(loader=FileSystemLoader('html_json_config'))  # 假设你的模板文件在'templates'文件夹中

html_template_path = "index.html"
html_view_json = "html_json_config/task_view.json"


@app.get("/")
async def read_root(request: Request):
    # 渲染模板，并将AMIS JSON传递给模板
    template = env.get_template(html_template_path)
    with open(html_view_json, "r", encoding="utf-8") as f:
        html_content = template.render(amis_json=f.read())
        return HTMLResponse(content=html_content, status_code=200)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
