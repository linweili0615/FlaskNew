#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from apps.auth import auth
# 获取数据库模型对象和SQLAlchemy对象db，注意不可使用App模块中的db
from apps.auth.models import *
from flask_login import login_user,logout_user,current_user,login_required
from apps.auth.forms import RegisterForm, LoginForm,TokenForm
from flask import app
from flask import request, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer,BadSignature, \
    SignatureExpired

@auth.route('/')
def index():
    return 'This Page Is auth'


@auth.route('/test')
@login_required
def test_token():
    return '333'

# 用户注册
@auth.route('/register/', methods=['POST'])
def register():
    print(request.get_json())
    print(request.get_data().decode('utf-8'))
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
    if request.method == 'GET':
        return 'login.html'

    if request.method == 'POST':
        form = LoginForm()
        if form.validate():
            # 根据用户名查找用户
            u = User.query.filter_by(username=form.username.data,password=form.password.data).first()
            if  u:
                login_user(u)
                token = generate_auth_token(u.id)
                return jsonify({'token':token})
        else:
            return jsonify({'msg':'params invalid'})

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return 'fds'

@auth.route('/validToken',methods=['POST'])
def valid_token():
    #解析token令牌信息
    form = TokenForm()
    if form.validate_on_submit():
        try:
            s = TimedJSONWebSignatureSerializer(app.config['SECRET_KEY'])
            data = s.loads(form.token.data, return_header=True)
            r = {
                'scope': data[0]['scope'],
                'create_at': data[1]['iat'],
                'expire_in': data[1]['exp'],
                'uid': data[0]['uid']
            }
            return jsonify(r)
        except SignatureExpired:
            return 'token is expired'
        except BadSignature:
            return 'token is invalid'
    return jsonify({
        "status": "failed",
        "error": form.errors
    })




#生成token字符串
def generate_auth_token(uid, scope=None, expiration=5000):
    #通过flask提供的对象，传入过期时间和flask的SECRET_KEY生成token令牌
    s = TimedJSONWebSignatureSerializer(app.config['SECRET_KEY'],
                                        expires_in=expiration)
    #uid唯一值表示当前请求的客户端
    #type表示客户端类型，看业务场景进行增删
    #scope权限作用域
    #设置过期时间，这个是必须的，一般设置两个小时
    return s.dumps({
        'uid': uid,
        'scope': scope
    }).decode('ascii')
















