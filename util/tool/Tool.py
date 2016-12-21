#!/bin/bash
# -*- coding=utf-8 -*-
import jieba.analyse
import re
import os
import sys

'''
@author liangzhicheng
@data 2016-12-19 9:16:00
'''


def createKeyWord(ResultPath, fileName, topK):
    '''
    使用tf-idf产生单词权重
    :param path:存放文件路径
    :param fileName:源文件
    :param topK:需要抽取的单词个数
    :return:
    '''
    source = 'D:\\workspace\\python-workspace\\MachineLearning\\util\\read\\source\\'
    result = file(ResultPath + fileName, 'w+')
    with open(source + fileName, 'rb') as f:
        for line in f:
            if line[:-1].strip():  # 去除空行
                filmName = line.strip().split(',')[0]
                filmDesc = gbk_2_utf8(''.join(line.strip().split(',')[1:]))
                content = ''
                result.write('\n')
                for w in jieba.analyse.extract_tags(rePunctuation(filmDesc), topK=topK):
                    content += "'" + w.encode('gbk') + "'" + ','
                result.write('[' + "'" + filmName + "'" + ',' + content[:-1] + ']' + ',')
    print fileName,'存放路径:', ResultPath
    result.close()


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
                    FileList.append(fn)
            else:
                fullfilename = os.path.join(FindPath, fn)  # 默认直接返回所有文件名
                FileList.append(fullfilename)
    if (len(FileList) > 0):  # 对文件名排序
        FileList.sort()
    return FileList


def utf8_2_gbk(str):
    '''
    utf-8转gbk
    :param str: 字符串
    :return: 转码后的字符串
    '''
    result = str.decode("utf-8").encode("gbk", "ignore")
    return result


def gbk_2_utf8(str):
    '''
    gbk转utf-8
    :param str: 字符串
    :return: 转码后的字符串
    '''
    result = str.decode("gbk").encode("utf-8", "ignore")
    return result
