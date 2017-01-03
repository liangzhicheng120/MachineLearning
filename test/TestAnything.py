#!/bin/bash
# -*- coding=utf-8 -*-
'''
@author liangzhicheng
@data 2017-01-03 13:37:00
'''
import hashlib
from functools import wraps
import time

db = {}

# 信息字典
LOGIN_DICT = {'ERROR': 'login failed,cause by wrong password', 'SUCCESS': 'login success', 'INDEX': 'please login'}
REGISTER_DICT = {'ERROR': 'Entering the password twice is not the same', 'SUCCESS': 'regisration success'}
INFORMATION = {'INFO': 'Do you want to log in now:(y|n)', 'PASSWORD': 'please input password:',
               'USERNAME': 'please input username:', 'REPASSWORD': 'please input password again:'}
USER_DICT = {'NAME': 'name:', 'PASSWORD': 'password:'}


# 加密验证
def MD5(data):
    md5 = hashlib.md5()
    md5.update(data)
    return md5.hexdigest()


# 计算程序运行时间
def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.clock()
        result = function(*args, **kwargs)
        t1 = time.clock()
        print ("Total time running %s: %s s" % (function.func_name, str(t1 - t0)))
        return result

    return function_timer


# 登录注册
@fn_timer
def register(username, password1, password2):
    def login(name, pawd):
        print LOGIN_DICT['INDEX']
        if MD5(pawd) == db[name]:
            print LOGIN_DICT['SUCCESS']
        else:
            print LOGIN_DICT['ERROR']

    if password1 == password2:
        db[str(username)] = MD5(password1)
        print REGISTER_DICT['SUCCESS']
        if raw_input(INFORMATION['INFO']) == 'y':
            login(name=raw_input(USER_DICT['NAME']), pawd=raw_input(USER_DICT['PASSWORD']))
        else:
            exit()
    else:
        print REGISTER_DICT['ERROR']
        exit()


if __name__ == '__main__':
    register(username=raw_input(INFORMATION['USERNAME']),
             password1=raw_input(INFORMATION['PASSWORD']),
             password2=raw_input(INFORMATION['REPASSWORD']))
