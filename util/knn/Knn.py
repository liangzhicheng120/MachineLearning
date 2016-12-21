#!/bin/bash
# -*- coding: utf-8 -*-
'''
@author liangzhicheng
@data 2016-12-19 9:16:00
'''
from numpy import *
import operator


# KNN 分类算法
def classify0(inx, dataSet, labels, k):
    '''
    group= array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels =['A', 'A', 'B', 'B']
    relust = classify0([0, 0], group, labels, 3)
    :param inx:
    :param dataSet:
    :param labels:
    :param k:
    :return:
    '''
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inx, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distance = sqDistances ** 0.5
    # 输出欧式距离
    # print distance
    sortedDistIndecies = distance.argsort()  # 增序排序
    classCount = {}
    for i in range(k):
        # 获取类别
        voteIlabel = labels[sortedDistIndecies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        # 对字典中的类别出现次数进行排序，classCount中存储的事 key-value，其中key就是label，value就是出现的次数
        # 所以key=operator.itemgetter(1)选中的事value，也就是对次数进行排序
        sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    # sortedClassCount[0][0]也就是排序后的次数最大的那个label
    return sortedClassCount[0][0]

# 实例
# def createDataSet():
#     group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
#     lables = ['A', 'A', 'B', 'B']
#     return group, lables

# if __name__ == '__main__':
#     group, labels = createDataSet();
#     # print createDataSet()
#     relust = classify0([0, 0], group, labels, 3)
#     print 'the classify relust is :', relust
