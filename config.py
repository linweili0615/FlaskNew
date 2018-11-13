#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

BASE_DIR = os.getcwd()  # 项目的绝对路径
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')  # 模板文件的路径
STATICFILES_DIR = os.path.join(BASE_DIR, 'static')  # 静态文件的路径
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456a@192.168.1.3:3306/fn'  # 数据库URI
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'linweili'
JSON_AS_ASCII = False
