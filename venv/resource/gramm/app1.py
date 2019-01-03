#!/user/bin/env python
# -*- coding: utf-8 -*-
# @TIME   :2018/11/16 16:12
# @Author :Sunminy
# @File   :app1.py
#encoding :utf-8
import os

from flask import make_response,Flask

from zutnlp_text.venv.Flask.grammar1 import app

app = Flask(__name__)

@app.route('/')
#装饰器，做一个URL与视图函数的映射

def index():

    with open('graout.txt', encoding='utf-8', mode='r') as f:
       # resp = make_response(str(f.readlines()))
        resp = make_response(str(f.read()))
        resp.headers["Content-type"] = "text/plan;charset=UTF-8"
    return resp
if __name__ == '__main__':
    app.run(debug=True)
