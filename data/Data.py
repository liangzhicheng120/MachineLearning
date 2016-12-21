#!/bin/bash
# -*- coding: utf-8 -*-
'''
@author liangzhicheng
@data 2016-12-19 9:16:00
'''
import re
import os
import sys
import jieba.analyse
import jieba.posseg

stopwords = []
nr = 0
ns = 0
t = 0
a = 0
v = 0
nt = 0
nz = 0


def rePunctuation(str, code):
    '''
    去除句子中的特殊字符与数字
    :param str:
    :return:
    '''
    str = re.sub(r"\w|[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）《》=-“ ”」「]+".decode('utf-8', 'ignore'),
                 ' '.decode('utf-8', 'ignore'), str.decode(code))
    return str


if __name__ == '__main__':

    source = open(u'动画mini.csv', 'rb')

    with open(u'stopwords.txt', 'rb') as f:
        for line in f:
            stopwords.append(line.strip())
    for line in source:
        content = rePunctuation(''.join(line.strip().split(',')[1:]), 'gbk')

        # for w in jieba.posseg.cut(content):
        #     if 'nr' in w.encode('utf-8'):
        #         nr += 1
        #     if 'ns' in w.encode('utf-8'):
        #         ns += 1
        #     if 't' in w.encode('utf-8'):
        #         t += 1
        #     if 'a' in w.encode('utf-8'):
        #         t += 1
        #     if 'v' in w.encode('utf-8'):
        #         t += 1
        #     if 'nt' in w.encode('utf-8'):
        #         nt += 1
        #     if 'nz' in w.encode('utf-8'):
        #         nz += 1
        # print str(nr) + '\t' + str(ns) + '\t' + str(t) + '\t' + str(a) + '\t' + str(v) + '\t' + str(nt) + '\t' + str(nz)

        for w in jieba.analyse.extract_tags(content, topK=10):
            print w

    source.close()
