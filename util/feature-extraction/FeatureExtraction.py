#!/bin/bash
# -*- coding: utf-8 -*-
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances

'''
@author liangzhicheng
@data 2016-12-19 9:16:00
'''
str1 = '冒险 斯特兰 莫度 多维 男爵 车祸 能力 大火 真相 麻风病院 神奇 奇兽 珍奇 魔法 南太平洋 小岛 岛屿 部落 刀客 通缉 逃亡 沙漠 抢劫案 黑帮 劫匪 匪徒 重重围困 凶兽 掠食 雇佣兵 囚禁 勇士 公安人员 危在旦夕 暴风雪 被困'
str2 = '莫度 多维 男爵'
corpus = [
    str1, str2
]


# vectorizer = CountVectorizer()
# print(vectorizer.fit_transform(corpus).todense())
def test(corpus):
    counts = vectorizer.fit_transform(corpus).todense()
    for x, y in [[0, 1]]:
        dist = euclidean_distances(counts[x], counts[y])
        print('文档{}与文档{}的距离{}'.format(x, y, dist))
