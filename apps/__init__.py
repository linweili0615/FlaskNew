#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import config

# 初始化SQLAlchemy
db = SQLAlchemy()
loginmanager=LoginManager()
loginmanager.session_protection='strong'
loginmanager.login_view='auth.login'

def create_app():
    app =  Flask(__name__)
    app.config.from_object(config)
    # SQLAlchemy初始化App
    db.init_app(app)
    loginmanager.init_app(app)

    return app