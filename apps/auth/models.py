#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from apps import db

class Student(db.Model):  # 继承SQLAlchemy.Model对象，一个对象代表了一张表
    s_id= db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)  # id 整型，主键，自增，唯一
    s_name = db.Column(db.String(20))  # 名字 字符串长度为20
    s_age = db.Column(db.Integer, default=20)  # 年龄 整型，默认为20

    __tablename__ = 'student'  # 该参数可选，不设置会默认的设置表名，如果设置会覆盖默认的表名
    def __init__(self, name, age):  # 初始化方法，可以对对象进行创建
        self.s_name = name
        self.s_age = age
    def __repr__(self):  # 输出方法，与__str__类似，但是能够重现它所代表的对象
        return '<Student %r, %r, %r>' % (self.s_id, self.s_name, self.sage)