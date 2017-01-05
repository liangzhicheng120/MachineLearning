#!/bin/bash
# -*- coding=utf-8 -*-
'''
@author liangzhicheng
@data 2017-01-03 13:37:00
'''
import hashlib
from functools import wraps
import time

if __name__ == '__main__':
    with open('iril.csv', 'rb') as f:
        for line in f:
            content = line.strip().split(',')
            print content[0] + ',' + '1:' + content[1] + ' 2:' + content[2] + ' 3:' + content[3] + ' 4:' + content[4]
