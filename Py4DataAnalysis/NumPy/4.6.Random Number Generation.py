#!/usr/bin/env python3
# Filename:4.6. Random Number Generation.py

__author__ = 'JeromeYao'

'''
this's a note of <Python for Data Analysis> -- Wes McKinney
'''
print('\n4.6. Random Number Generation\n')
# numpy.random对python内置random做补充。
# 可以用normal来得到一个标准正态分布的4×4样本数组。
import numpy as np

samples = np.random.normal(size=(4, 4))
print(samples)

# 若使用python内置random函数一次只能生成一个样本值
from random import normalvariate

N = 1000000
'''
部分numpy.random函数
seed  确定随机数生成器的种子
permutation  返回一个序列的随机排列或返回一个随机排列的范围
shuffle  对一个序列就地随机排列
rand  产生均匀分布的样本值
normal  产生正态分布的样本值
beta  产生Beta分布的样本值
chisquare  产生卡方分布的样本值
gamma  产生Gamma分布的样本值
uniform  产生在[0, 1)中均匀分布的样本值
'''
print('\nExample: Random Walks\n')





























