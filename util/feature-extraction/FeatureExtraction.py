#!/bin/bash
# -*- coding: utf-8 -*-
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer

'''
@author liangzhicheng
@data 2016-12-19 9:16:00
'''
# 字符字典转换为特征数组(分类变量特征提取)
onehot_encoder = DictVectorizer()
instances = [{'城市': '韶关'}, {'城市': '广州'}, {'城市': '中山'}]
arr = onehot_encoder.fit_transform(instances).toarray()
# print arr


# 词库模型（Bag-of-words model）
corpus = [
    u'中国广东省广州市番禺区大学城',
    u'中国湖南省长沙篮球游戏'
]

vectorizer = CountVectorizer()
print vectorizer.fit_transform(corpus).todense()
for line in vectorizer.vocabulary_:
    print line
