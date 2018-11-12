#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from apps.auth.models import User


# 用户注册表单
class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='用户名不能为空'), Length(6, 12, message='用户名只能在6~12个字符之间')])
    password = PasswordField('密码', validators=[DataRequired(message='密码不能为空'), Length(6, 20, message='密码只能在6~20个字符之间')])
    submit = SubmitField('立即注册')

    # 自定义用户名验证器
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已注册，请选用其它名称')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(message='no empty')])
    password = PasswordField('password', validators=[DataRequired(message='no empty')])
    submit = SubmitField('login')