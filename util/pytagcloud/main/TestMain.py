#!/bin/bash
# -*- coding: utf-8 -*-
import codecs
import random
from pytagcloud import create_tag_image, create_html_data, make_tags, \
    LAYOUT_HORIZONTAL, LAYOUTS
from pytagcloud.colors import COLOR_SCHEMES
from pytagcloud.lang.counter import get_tag_counts
from operator import itemgetter

wd = {}

fp = codecs.open("rsa.txt", "r", 'utf-8');

alllines = fp.readlines();

fp.close();

for eachline in alllines:
    line = eachline.strip().split(' ')
    wd[line[0]] = float(line[1])
print wd

swd = sorted(wd.iteritems(), key=itemgetter(1), reverse=True)
tags = make_tags(swd, minsize=50, maxsize=240, colors=random.choice(COLOR_SCHEMES.values()))
create_tag_image(tags, 'cloud_0.png', background=(0, 0, 0, 255),
                 size=(2400, 1000), layout=LAYOUT_HORIZONTAL,
                 fontname="SimHei")
