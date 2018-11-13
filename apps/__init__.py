#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import config

# 初始化SQLAlchemy
db = SQLAlchemy()
loginmanager=LoginManager()
#认证加密程度
loginmanager.session_protection='strong'
#登陆认证的处理视图
loginmanager.login_view='auth.login'
#登陆提示信息
loginmanager.login_message=u'对不起，您还没有登录'
loginmanager.login_message_category='info'


def create_app():
    app =  Flask(__name__)
    app.config.from_object(config)
    # SQLAlchemy初始化App
    db.init_app(app)
    # 配置用户认证信息
    loginmanager.init_app(app)

    return app