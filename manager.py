#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask_script import Manager
from apps import create_app
from apps.auth import auth
from apps.test import test

# 创建app
app = create_app()
#注册蓝图
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(test, url_prefix='/test')

manager = Manager(app)

if __name__ == '__main__':
    manager.run()