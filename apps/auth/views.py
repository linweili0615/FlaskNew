#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from apps.auth import auth
# 获取数据库模型对象和SQLAlchemy对象db，注意不可使用App模块中的db
from apps.auth.models import *
from flask_login import login_user,logout_user,current_user,login_required
from apps.auth.forms import RegisterForm, LoginForm
from apps import db

@auth.route('/')
def index():
    return 'This Page Is auth'



# 用户注册
@auth.route('/register/', methods=['POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # 根据表单数据创建用户对象
        u = User(username=form.username.data,
                 password=form.password.data)
        # 将用户对象保存到数据库
        db.session.add(u)
        # 下面生成token需要用户id，此时还没有id，需要手动提交
        db.session.commit()

        return 'ok'
    return 'bu xing'



# 用户登录
@auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 根据用户名查找用户
        u = User.query.filter_by(username=form.username.data).first()
        if  u:
            return ' login ok'

    return 'login'