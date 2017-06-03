#!/usr/bin/env python3
# Filename:initial_script.py

"""
Instruction:该脚本适用于建立有规律的文件集。
一级目录（脚本所在目录）->二级目录->文件
example: NOP3C->C08->NOP3C_C08_P12.py
"""

import os

__author__ = 'JeromeYao'

pwd = os.getcwd()  # 获取当前脚本所在文件路径

name0 = pwd.split('/')[-1]  # 上级文件夹名称

num_begin_cha, num_end_cha = input('输入开始和结束的章节号(以逗号分割)').split(',')

range_cha = range(int(num_begin_cha), int(num_end_cha)+1)  # 根据章节数最大最小值转化为一个范围

[*num_files] = input('每个章节有几个段落?(以逗号分割)').split(',')

for i in range_cha:  # 根据章节个数做循环操作
    i0 = str(i).zfill(2)  # i0 以0补位
    name_dir = 'C' + i0
    os.mkdir(name_dir) if not os.path.isdir(name_dir) else print('文件夹' + name_dir + '已存在')  # 创建文件夹
    os.chdir(name_dir)  # 进入该文件夹
    for j in num_files:  # 根据文件数列表内容做循环操作
        for k in range(1, int(j)+1):
            k0 = str(k).zfill(2)  # 以0补位
            name_file = name0 + '_' + name_dir + '_' + 'P' + k0 + '.py'
            with open(name_file, 'w') as f:  # 打开或新建文件，自带关闭
                input_lines = '#!/usr/bin/env python3\n# Filename:' + name_file  # 文件输入的初始化内容
                f.write(input_lines)  # 写入内容
    os.chdir('..')  # 返回上级文件夹

print('**创建完成**')


