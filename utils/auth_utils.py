#/usr/bin/env python3
#coding=utf-8
from flask import current_app, g, request
from flask_httpauth import HTTPAuth
from itsdangerous import TimedJSONWebSignatureSerializer,BadSignature, SignatureExpired

auth = HTTPAuth()
