#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from apps import db
from flask_login import UserMixin
from apps import loginmanager

class User(db.Model, UserMixin):  # 继承SQLAlchemy.Model对象，一个对象代表了一张表
    __tablename__ = 'users'
    id = db.Column(db.String(64), primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(28))

    # 注意！这里必须重写，因为源码使用unicode(id)，但是python3没有unicode()方法！此时就无法登录用户！
    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

#用户认证的回调函数
@loginmanager.user_loader
def load_user(user_id):
    return User.query.get(id=user_id)