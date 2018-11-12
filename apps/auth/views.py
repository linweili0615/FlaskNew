#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from apps.auth import auth
# 获取数据库模型对象和SQLAlchemy对象db，注意不可使用App模块中的db
from apps.auth.models import *

@auth.route('/')
def index():
    return 'This Page Is auth'