#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from apps import db

class Users(db.Model):  # 继承SQLAlchemy.Model对象，一个对象代表了一张表
    s_id= db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)  # id 整型，主键，自增，唯一
    s_name = db.Column(db.String(20))  # 名字 字符串长度为20
    s_age = db.Column(db.Integer, default=20)  # 年龄 整型，默认为20

    __tablename__ = 'users'