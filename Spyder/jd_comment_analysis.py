#!usr/bin/env python3
# Filename:  jd_comment_analysis.py

import json
import pandas as pd

__author__ = 'JeromeYao'


def read_data(path):
    for line in open(path):
        r = json.loads(line)
        for j in r['comments']:
            print('时间: {}'.format(j['creationTime']))
            print('颜色: {}'.format(j['productColor']))
            print('规格: {}'.format(j['productSize']))
            print('用户: {}'.format(j['userClientShow']))
            print('等级: {}'.format(j['userLevelName']))
            print('评分: {}'.format(j['score']))
            print('内容: {}'.format(j['content']))
            print('============================================')

path_jd_comments = "/home/jerome/GitEnvy4/PyNotes/Spyder/data_JD.json"
read_data(path_jd_comments)
