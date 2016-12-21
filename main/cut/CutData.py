#!/bin/bash
# -*- coding: utf-8 -*-
import re
import sys
import os

sys.path.append('D:\\workspace\\python-workspace\\MachineLearning\\util\\tool')
import Tool as t

'''
@author liangzhicheng
@data 2016-12-19 10:00:00
'''

if __name__ == '__main__':
    spath = sys.path[0] + '\\source\\'
    rpath = sys.path[0] + '\\cluster\\'
    typeDict = {}
    resultDict = {}
    for fileName in t.GetFileList(spath, FlagStr=['csv']):
        with open(spath + fileName, 'rb') as f:
            for line in f:
                fileType = line.strip().split(',')[0]
                fileDesc = line.strip().split(',')[1:]
                typeDict[fileType] = typeDict.get(fileType, '') + ','.join(fileDesc) + '\n'
        for key, value in typeDict.items():
            result = file(rpath + key + '.txt', 'w+')
            result.write(value)
            result.close()
