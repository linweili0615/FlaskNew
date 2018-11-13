#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from apps.auth import auth
# 获取数据库模型对象和SQLAlchemy对象db，注意不可使用App模块中的db
from apps.auth.models import *
from flask_login import login_user,logout_user,current_user,login_required
from apps.auth.forms import RegisterForm, LoginForm,TokenForm
from apps import create_app
from flask import request, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer,BadSignature, \
    SignatureExpired
import uuid, json
@auth.route('/')
def index():
    return 'This Page Is auth'


@auth.route('/test')
@login_required
def test_token():
    return '333'

# 用户注册
@auth.route('/register', methods=['POST'])
def register():
    if request.get_data() is not None:
        try:
            json_data = json.loads(request.get_data().decode('utf-8'))
        except BaseException:
            return jsonify({'status': 'fail', 'msg': '参数格式错误'})
        if json_data['username'] is not None and json_data['password'] is not None:
            u = User.query.filter_by(username=json_data['username']).first()
            if not u:
                id = str(uuid.uuid4())
                # nUser = User()
                # nUser.id = id
                # nUser.username = json_data['username']
                # nUser.password = json_data['password']
                nUser = User(id=id,username=json_data['username'],password=json_data['password'])
                try:
                    db.session.add(nUser)
                    db.session.commit()
                    login_user(nUser)
                    token = generate_auth_token(id)
                    return jsonify({'status': 'success', 'id': id, 'username': json_data['username'],
                                    'token': token})
                except BaseException:
                    db.session.rollback()
                    return jsonify({'status': 'fail', 'msg': '用户信息写入失败'})
            return jsonify({'status': 'fail', 'msg': '该用户已存在'})
        return jsonify({'status': 'fail', 'msg': '用户信息不能为空'})
    return jsonify({'status':'fail','msg': '参数不能为空'})



# 用户登录
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 'login.html'

    if request.method == 'POST':
        try:
            json_data = json.loads(request.get_data().decode('utf-8'))
        except BaseException as e:
            return jsonify({'status': 'fail', 'msg': '参数格式错误'})
        if json_data['username'] and json_data['password']:
            # 根据用户名查找用户
            u = User.query.filter_by(username=json_data['username'], password=json_data['password']).first()
            if u:
                login_user(u)
                token = generate_auth_token(u.id)
                return jsonify({'status': 'success', 'id': u.id, 'username': json_data['username'], 'token': token})
            jsonify({'status': 'fail', 'msg': '用户名或密码错误'})
        return jsonify({'status': 'fail', 'msg': '用户信息不能为空'})




@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return 'fds'

@auth.route('/validToken',methods=['POST'])
def valid_token():
    #解析token令牌信息
    try:
        json_data = json.loads(request.get_data().decode('utf-8'))
    except BaseException as e:
        return jsonify({'status': 'fail', 'msg': '参数格式错误'})
    try:
        app = create_app()
        s = TimedJSONWebSignatureSerializer(app.config['SECRET_KEY'])
        data = s.loads(json_data['token'], return_header=True)
        u = User.query.filter_by(id=data[0]['uid']).first()
        r = {
            'status': 'success',
            'username': u.username,
            'token': json_data['token']
        }
        return jsonify(r)
    except SignatureExpired:
        return jsonify({'status': 'fail', 'msg': 'token已过期'})
    except BadSignature:
        return jsonify({'status': 'fail', 'msg': 'token无效'})

#生成token字符串
def generate_auth_token(uid, scope=None, expiration=5000):
    app = create_app()
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
















