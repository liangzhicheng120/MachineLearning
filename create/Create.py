#!/bin/bash
# -*- coding: utf-8 -*-

from __future__ import division
import re
import os
import sys
import jieba.analyse
import dataSet as da

'''
@author liangzhicheng
@data 2016-12-19 9:16:00
'''

count = 0


def createKeySet(FileName):
    '''
    生成语料库
    :param FileName:
    :return: [词语列表,词语数量]
    '''
    resultSet = set()
    path = sys.path[0] + '\\source\\'
    with open(path + FileName, 'rb') as f:
        for line in f:
            if line[:-1].strip():
                try:
                    resultSet.add(line.strip().lower())
                except Exception, e:
                    resultSet.add(line.strip().lower().decode('gbk').encode('utf-8', 'ignore'))
    result = list(resultSet)
    return [result, len(result)]


def countKeyWords(dataRow, wordsLabel):
    '''
    统计出现关键词次数
    :param dataSet: 数据集
    :param wordsLabel: 标签词
    :return:
    '''
    count = 0
    keyList, keyLen = createKeySet(wordsLabel)
    for w in keyList:
        if w in dataRow:
            count += 1
    return count / keyLen


if __name__ == '__main__':
    print countKeyWords(dataRow=da.str1, wordsLabel=u'动画.txt')
    print countKeyWords(dataRow=da.str1, wordsLabel=u'动作.txt')
    print countKeyWords(dataRow=da.str1, wordsLabel=u'冒险.txt')
    print countKeyWords(dataRow=da.str1, wordsLabel=u'喜剧.txt')
    print countKeyWords(dataRow=da.str1, wordsLabel=u'悬疑.txt')
    print countKeyWords(dataRow=da.str1, wordsLabel=u'战争.txt')
    print countKeyWords(dataRow=da.str1, wordsLabel=u'武侠.txt')
    print countKeyWords(dataRow=da.str1, wordsLabel=u'爱情.txt')
    print countKeyWords(dataRow=da.str1, wordsLabel=u'科幻.txt')
