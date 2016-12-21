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


def test(dataRow):
    result = []
    result.append(countKeyWords(dataRow=dataRow, wordsLabel=u'动画.txt'))
    result.append(countKeyWords(dataRow=dataRow, wordsLabel=u'动作.txt'))
    result.append(countKeyWords(dataRow=dataRow, wordsLabel=u'冒险.txt'))
    result.append(countKeyWords(dataRow=dataRow, wordsLabel=u'喜剧.txt'))
    result.append(countKeyWords(dataRow=dataRow, wordsLabel=u'悬疑.txt'))
    result.append(countKeyWords(dataRow=dataRow, wordsLabel=u'战争.txt'))
    result.append(countKeyWords(dataRow=dataRow, wordsLabel=u'武侠.txt'))
    result.append(countKeyWords(dataRow=dataRow, wordsLabel=u'爱情.txt'))
    result.append(countKeyWords(dataRow=dataRow, wordsLabel=u'科幻.txt'))
    return '\t'.join(map(lambda x: str(x), result))


if __name__ == '__main__':
    print test(dataRow=da.str1)
    print test(dataRow=da.str2)
    print test(dataRow=da.str3)
    print test(dataRow=da.str4)
    print test(dataRow=da.str5)
    print test(dataRow=da.str6)
    print test(dataRow=da.str7)
    print test(dataRow=da.str8)
    print test(dataRow=da.str9)
    print test(dataRow=da.str10)
    print test(dataRow=da.str11)
    print test(dataRow=da.str12)
    print test(dataRow=da.str13)
    print test(dataRow=da.str14)
    print test(dataRow=da.str15)
    print test(dataRow=da.str16)
    print test(dataRow=da.str17)
    print test(dataRow=da.str18)