#!/bin/bash
# coding=utf-8
import os
import re
import sys
import jieba.analyse
from numpy import *
import Knn as k


def rePunctuation(str):
    '''
    去除句子中的特殊字符与数字
    :param str:
    :return:
    '''
    str = re.sub(r"\w|[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）《》=-“ ”」「]+".decode('utf-8', 'ignore'),
                 ' '.decode('utf-8', 'ignore'), str.decode('utf-8'))
    return str


def IsSubString(SubStrList, Str):
    '''''
    #判断字符串Str是否包含序列SubStrList中的每一个子字符串
    #>>>SubStrList=['F','EMS','txt']
    #>>>Str='F06925EMS91.txt'
    #>>>IsSubString(SubStrList,Str)#return True (or False)
    '''
    flag = True
    for substr in SubStrList:
        if not (substr in Str):
            flag = False
    return flag


def GetFileList(FindPath, FlagStr=[]):
    '''''
    #获取目录中指定的文件名
    #>>>FlagStr=['F','EMS','txt'] #要求文件名称中包含这些字符
    #>>>FileList=GetFileList(FindPath,FlagStr) #
    '''
    FileList = []
    FileNames = os.listdir(FindPath)
    if (len(FileNames) > 0):
        for fn in FileNames:
            if (len(FlagStr) > 0):
                if (IsSubString(FlagStr, fn)):  # 返回指定类型的文件名
                    # fullfilename = os.path.join(FindPath, fn)
                    FileList.append(fn)
            else:
                fullfilename = os.path.join(FindPath, fn)  # 默认直接返回所有文件名
                FileList.append(fullfilename)
    if (len(FileList) > 0):  # 对文件名排序
        FileList.sort()

    return FileList


def getNum(content):
    result = ''
    for line in content:
        result += str(line[1]) + ','
    return '[' + result[:-1] + ']' + ',' + '\n'


def createNumpy():
    '''
    生成矩阵向量
    :return:
    '''
    spath = sys.path[0] + '\\source\\'
    npath = sys.path[0] + '\\numpy\\'
    source = GetFileList(spath, ['txt'])
    for fileName in source:
        result = file(npath + fileName, 'w+')
        with open(spath + fileName, 'rb') as f:
            for line in f:
                line = rePunctuation(line.strip())
                result.write(getNum(jieba.analyse.extract_tags(line, topK=2, withWeight=True)))
    result.close()


if __name__ == '__main__':
    createNumpy()
    #
    # group = array([
    #     [0.449533356179, 0.437883744878],
    #     [0.523681958867, 0.356427632103],
    #     [0.416465607366, 0.371759501536],
    #     [0.51871585637, 0.223605894626],
    #     [0.20728579001, 0.204771090846],
    #     [0.326039113715, 0.227534241653],
    #     [1.11207139562, 0.417026773357],
    #     [0.857100430229, 0.4695013216],
    #     [0.385871749386, 0.273270723652],
    #     [0.587939385389, 0.391959590259],
    #     [0.381636700272, 0.303215463672],
    #     [0.857100430229, 0.4695013216],
    #     [0.569274642995, 0.362405428641],
    #     [0.527325679853, 0.19145386001],
    #     [0.664153750161, 0.583077532866],
    #     [0.524331908022, 0.323453677355],
    #     [0.893167350928, 0.67144266509],
    #     [0.569274642995, 0.379516428663],
    #     [0.368612695263, 0.177348351534],
    #     [0.452930634276, 0.327268058992],
    #     [0.756630854614, 0.594854587119],
    #     [0.489249219503, 0.241510454604],
    #     [0.365039821076, 0.357076141079],
    #     [0.365039821076, 0.357076141079],
    #     [0.36891547693, 0.257775230597],
    #     [0.731546592189, 0.397162218629],
    #     [0.27169926143, 0.217201641594],
    #     [0.314373246285, 0.189611868044],
    #     [0.695283746145, 0.379595944107],
    #     [0.556611537535, 0.513966787404],
    #     [0.555766988968, 0.223471130195],
    #     [0.597738375145, 0.514487986965],
    #     [0.821319904779, 0.198055058563],
    #     [0.818819691979, 0.818819691979]
    # ])
    #
    # lables = [u'冒险', u'冒险', u'冒险', u'剧情', u'剧情', u'剧情', u'剧情', u'剧情', u'剧情', u'剧情', u'剧情', u'剧情', u'剧情', u'剧情', u'剧情',
    #           u'剧情', u'剧情', u'剧情', u'剧情', u'剧情', u'剧情', u'动作', u'动作', u'动作', u'动作', u'动画', u'动画', u'动画', u'喜剧', u'喜剧',
    #           u'喜剧', u'喜剧', u'喜剧', u'喜剧', u'喜剧', u'喜剧', u'喜剧', u'喜剧', u'喜剧', u'喜剧', u'喜剧', u'喜剧', u'恐怖', u'恐怖', u'恐怖',
    #           u'恐怖', u'恐怖', u'恐怖', u'恐怖', u'武侠', u'爱情', u'爱情', u'爱情', u'爱情', u'爱情']
    #
    # print k.classify0([0.818819691979, 0.818819691979], group, lables, 3)
