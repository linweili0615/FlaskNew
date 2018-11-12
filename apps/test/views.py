#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from apps.test import test
# 获取数据库模型对象和SQLAlchemy对象db，注意不可使用App模块中的db
from apps.test.models import *

@test.route('/')
def index():
    return 'This Page Is test'