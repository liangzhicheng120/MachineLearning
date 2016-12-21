#!/bin/bash
# -*- coding: utf-8 -*-
'''
@author liangzhicheng
@data 2016-12-19 9:16:00
'''
from numpy import *
import operator
import Knn as k
import KnnData as kd

if __name__ == '__main__':
    group, labels = kd.createDataSet()
    clazz = [0.645483793488, 0.628756146492]
    relust = k.classify0(clazz, group, labels, 3)
    print 'the classify relust is :', relust
