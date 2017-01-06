#!/bin/bash
# -*- coding=utf-8 -*-
'''
@author liangzhicheng
@data 2017-01-06 16:37:00
'''
import urllib2
from bs4 import BeautifulSoup
import re


def write_2_floder(url):
    content = urllib2.urlopen(url).read()
    with open(url[-14:], 'wb') as code:
        code.write(content)
    return 'finish!'


url = 'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.u79yxp&id=17540507116&skuId=3267912317844&areaId=330900&user_id=880734502&cat_id=2&is_b=1&rn=17b99e353f26eb6f42b88670e9a6d11c'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "html.parser")
imgList = map(lambda img: 'http:' + img.get('src'), soup.find_all(id='J_ImgBooth'))
print ''.join(map(write_2_floder, imgList))
