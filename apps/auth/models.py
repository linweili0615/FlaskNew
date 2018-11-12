#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from apps import db
from flask_login import UserMixin

class User(db.Model, UserMixin):  # 继承SQLAlchemy.Model对象，一个对象代表了一张表
    __tablename__ = 'users'
    id = db.Column(db.String(64), primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(28))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id