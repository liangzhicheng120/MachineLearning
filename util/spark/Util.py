#!/bin/bash
# -*- coding: utf-8 -*-
import sys
from operator import add
from pyspark import SparkContext, SparkConf
import time
from functools import wraps

'''
@author liangzhicheng
@data 2016-12-19 9:16:00
'''


def WordCount():
    sc = SparkContext(appName="PythonWordCount")
    lines = sc.textFile('words.txt')
    counts = lines.flatMap(lambda x: x.split(' ')) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print "%s: %i" % (word, count)
    sc.stop()


def fn_timer(function):
    '''
    计算程序运行时间
    :param function:
    :return:
    '''

    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.clock()
        result = function(*args, **kwargs)
        t1 = time.clock()
        print ("Total time running %s: %s s" % (function.func_name, str(t1 - t0)))
        return result

    return function_timer
