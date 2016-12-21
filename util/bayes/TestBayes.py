#!/bin/bash
# -*- coding: utf-8 -*-
import sys
import Bayes as nb
import BayesData as bd
import os

sys.path.append('D:\\workspace\\python-workspace\\MachineLearning\\util\\tool')
import Tool as t

'''
@author liangzhicheng
@data 2016-12-19 9:16:00
'''


def initBayes():
    t.createKeyWord(sys.path[0] + '\\source\\', u'冒险.txt', 3)
    t.createKeyWord(sys.path[0] + '\\source\\', u'剧情.txt', 3)
    t.createKeyWord(sys.path[0] + '\\source\\', u'动作.txt', 3)
    t.createKeyWord(sys.path[0] + '\\source\\', u'动画.txt', 3)
    t.createKeyWord(sys.path[0] + '\\source\\', u'喜剧.txt', 3)
    t.createKeyWord(sys.path[0] + '\\source\\', u'恐怖.txt', 3)
    t.createKeyWord(sys.path[0] + '\\source\\', u'惊悚.txt', 3)
    t.createKeyWord(sys.path[0] + '\\source\\', u'武侠.txt', 3)
    t.createKeyWord(sys.path[0] + '\\source\\', u'爱情.txt', 3)


def testBayes(testEntrys, *arg):
    '''

    :param testEntrys:
    :param arg: 预期值
    :return:
    '''
    clazz = {}
    count = 0
    for testEntry in testEntrys:
        clazzKey = nb.testingNB(loadDataSet=bd.loadDataSet('DC'), testEntry=testEntry)
        clazz[clazzKey] = clazz.get(clazzKey, 0) + 1
        if arg[0][0] == clazzKey:
            count += 1
        print clazzKey
    if len(arg) != 0:
        val = count / arg[0][1]  # 计算准确率
        print 'Accuracy Rate:', str("%.2f%%" % (val * 100))


if __name__ == '__main__':
    # initBayes()
    testEntry = ['罗曼蒂克消亡史', '初才', '香港', '坐上去']
    numpyVal = []
    DC = nb.testingNB(loadDataSet=bd.loadDataSet('DC'), testEntry=testEntry)
    if DC == 1:
        numpyVal.append(1)
    else:
        numpyVal.append(0)
        AS = nb.testingNB(loadDataSet=bd.loadDataSet('AS'), testEntry=testEntry)
        if AS == 1:
            numpyVal.append(1)
        else:
            numpyVal.append(0)
            CD = nb.testingNB(loadDataSet=bd.loadDataSet('CD'), testEntry=testEntry)
            if CD == 1:
                numpyVal.append(1)
            else:
                numpyVal.append(0)
                L = nb.testingNB(loadDataSet=bd.loadDataSet('L'), testEntry=testEntry)
                if L == 1:
                    numpyVal.append(1)
                else:
                    numpyVal.append(0)

    print numpyVal