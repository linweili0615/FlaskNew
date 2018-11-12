#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


# 初始化SQLAlchemy
db = SQLAlchemy()

def create_app():
    app =  Flask(__name__)
    app.config.from_object(config)
    # SQLAlchemy初始化App
    db.init_app(app)
    # 在这还可以设置好配置后， 初始化其他的模块

    return app