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


str1='11月4日至6日，中共中央政治局常委、国务院总理李克强在黑龙江同江、抚远、哈尔滨等地考察。这是4日傍晚，李克强来到同江银川乡幸福大院，察看洪灾后五保户和特困户安置情况。 新华社记者 黄敬文 摄11月4日至6日，中共中央政治局常委、国务院总理李克强在黑龙江同江、抚远、哈尔滨等地考察。今夏，黑龙江部分地区遭受严重洪涝灾害，近9万户群众的房屋损毁或倒塌。眼下临近隆冬，灾区又地处严寒地带，正值过冬安置的关键时刻，受灾群众能不能安全温暖过冬，李克强十分牵挂。他来到受灾最严重的同江市八岔赫哲族村，踩着泥泞湿滑的道路，查看村民房屋状况和越冬准备情况。他对围拢来的群众说，你们这里洪灾发生后，党中央国务院高度重视，习近平总书记等中央领导同志作出批示，省委、省政府带领大家奋力抢险救灾，做了大量艰苦细致的工作，取得了抗洪救灾的胜利，没有因灾死亡一个人。他特别叮嘱当地干部，这里冬天冰天雪地，最低温度达零下40摄氏度，要把排查工作做细做深做到位，看群众房屋安不安全，保暖程度够不够，绝不能让一个群众受冻，使大家住得保暖、住得保险。暮色渐浓，李克强走进安置受灾五保户和特困户的银川乡幸福大院，看到新建的安置房里暖融融的，他十分高兴。他对周围的群众说，党和政府惦记你们的冷暖，我们一起努力共渡难关、重建家园。冬天过暖和了，来年一定有好春天、好日子。考察回到驻地，李克强又立即召开工作会，进一步部署做好群众越冬、灾后重建、水毁工程修复和今冬明春农业生产等工作。'

my1 = jieba.analyse.extract_tags(str1, topK=8, withWeight=False, allowPOS=('ns', 'n', 'v', 'nv'))
for w in my1:
    print w
