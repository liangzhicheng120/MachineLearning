#!/bin/bash
# -*- coding: utf-8 -*-

'''
@author liangzhicheng
@data 2016-12-19 9:16:00
'''
import re
import os
import sys
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')


def exeSql(fileName, Sql):
    result = open(fileName, 'w+')
    conn = MySQLdb.connect(host='172.16.10.30', port=3306, user='test', passwd='meizu.com', db='MEIZU_CAL',
                           charset='utf8')
    cursor = conn.cursor()
    cursor.execute(Sql)
    results = cursor.fetchall()
    for row in results:
        result.writelines('\t'.join(list(row)) + '\n')
    result.close()
    cursor.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # Sql = 'SELECT FTITLE,FEXT,FDESC FROM MEIZU_CAL.T_NEW_COLUMN where FPARENTID = 6'
    Sql = "SELECT FTITLE,FEXT,FDESC FROM MEIZU_CAL.T_NEW_COLUMN where FPARENTID = 7 and FDESC != ''"
    exeSql('teleplay.txt', Sql)
