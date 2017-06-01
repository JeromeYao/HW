#!/usr/bin/env python3
# Filename:initial_script.py

import os

__author__ = 'JeromeYao'

pwd = os.getcwd()

name0 = pwd.split('/')[-1]

num_begin_cha, num_end_cha = input('输入开始和结束的章节号(以逗号分割)').split(',')

range_cha = range(int(num_begin_cha), int(num_end_cha)+1)

[*num_files] = input('每个章节有几个段落?(以逗号分割)').split(',')

for i in range_cha:
    i0 = str(i).zfill(2)
    name_dir = 'C' + i0
    os.mkdir(name_dir) if not os.path.isdir(name_dir) else print('文件夹' + name_dir + '已存在')
    os.chdir(name_dir)
    for j in num_files:
        for k in range(1, int(j)+1):
            k0 = str(k).zfill(2)
            name_file = name0 + '_' + name_dir + '_' + 'P' + k0 + '.py'
            with open(name_file, 'w') as f:
                f.write('#!/usr/bin/env python3\n# Filename:' + name_file)
    os.chdir('..')

print('**创建完成**')

# 3,15
# 16,16,21,13,12,25,25,15,13,14,15,14,21
