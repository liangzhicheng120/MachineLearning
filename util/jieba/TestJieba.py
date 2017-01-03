#!/bin/bash
# -*- coding: utf-8 -*-
import jieba.analyse
import re
import os
import sys

'''
@author liangzhicheng
@data 2016-12-19 9:16:00
'''
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Precise Mode: " + "/".join(seg_list))  # 精确模式，默认状态下也是精确模式
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造。")  # 搜索引擎模式
# print("Search Mode: " + "/".join(seg_list))
#
# jieba.suggest_freq(("中", "将"), tune=True)
# print("/".join(jieba.cut("如果放到post中将出错。", HMM=False)))
#
# jieba.add_word("江大桥", freq=20000, tag=None)
# print "/".join(jieba.cut("江州市长江大桥参加了长江大桥的通车仪式。"))

# my = jieba.analyse.textrank("江州市长江大桥参加了长江大桥的通车仪式。", topK=20, withWeight=False, allowPOS=('ns', 'n', 'v', 'nv'))
# for w in my:
#     print w
str1 = '在一座与世隔绝的孤岛上，曾经隔离着上百名麻风病患者，三十年前的一场大火，将这里的麻风病院化为灰烬，大火本身已渐成传说。三十年后，警校学生殷浩（张一山 饰）为在自己的女朋友，电影编导系学生小暖（丁丁 饰）面前显示自己男人的一面，带着她登上了隔离岛，拍摄纪录片，探寻大火真相。已经被人遗忘的隔离岛突然风浪骤起，死火复燃，殷浩和小暖“致命真相”的旅程由此开启......'
my1 = jieba.analyse.extract_tags(str1, topK=3, withWeight=False, allowPOS=('ns', 'n', 'v', 'nv'))
for w in my1:
    print w
