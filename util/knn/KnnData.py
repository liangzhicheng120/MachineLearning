#!/bin/bash
# -*- coding: utf-8 -*-
from numpy import *
import os
import re
import sys

'''
@author liangzhicheng
@data 2016-12-19 9:16:00
'''
# 7
donghua = [
    [11, 1, 60, 0, 0, 0, 4],
    [15, 3, 75, 0, 0, 0, 4],
    [29, 9, 116, 0, 0, 0, 5],
    [34, 16, 186, 0, 0, 0, 5],
    [47, 25, 253, 0, 0, 1, 8],
    [54, 28, 276, 0, 0, 1, 10],
    [59, 33, 322, 0, 0, 1, 11]
]
# 7
zhanzhen = [
    [7, 4, 24, 0, 0, 0, 2],
    [11, 7, 44, 0, 0, 0, 4],
    [16, 8, 52, 0, 0, 0, 5],
    [40, 21, 371, 0, 0, 0, 8],
    [48, 22, 385, 0, 0, 0, 12],
    [49, 29, 412, 0, 0, 0, 16],
    [62, 30, 449, 0, 0, 0, 18]
]
# 11
aiqing = [
    [5, 0, 21, 0, 0, 0, 0],
    [23, 1, 60, 0, 0, 0, 0],
    [24, 1, 83, 0, 0, 0, 2],
    [26, 5, 105, 0, 0, 0, 2],
    [26, 5, 111, 0, 0, 0, 5],
    [42, 5, 162, 0, 0, 0, 5],
    [42, 5, 174, 0, 0, 0, 5],
    [45, 6, 187, 0, 0, 0, 6],
    [46, 6, 203, 0, 0, 0, 8],
    [57, 6, 230, 0, 0, 0, 8],
    [68, 6, 257, 0, 0, 0, 8]
]


def createDataSet():
    group = array(donghua + zhanzhen + aiqing)
    lables = tuples_2_numpy([[7, u'动画'],
                             [7, u'战争'],
                             [11, u'爱情']
                             ])
    return group, lables


def tuples_2_numpy(data):
    '''
    [3,1] ===> [1,1,1]
    :param data:
    :return:
    '''
    classVec = []
    for tuples in data:
        number = tuples[0]
        element = tuples[1]
        for n in range(0, number):
            classVec.append(element)
    return classVec
