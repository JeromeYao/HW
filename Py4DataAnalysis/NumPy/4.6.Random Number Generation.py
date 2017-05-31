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

'''
这是一个利用数组操作来模拟随机游走的示例程序。
让我们先来看一个简单的随机游走的例子，从0开始，
步长为1和-1，且以相等的概率出现。
一个纯Python方式来实现一个单一的有1000步的随机游走的方式是使用内建的 random 模块
'''

import random

position = 0

walk = [position]

steps = 1000

for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

'''
你可能会发现 walk 简单的把随机步长累积起来并且可以使用一个数组表达式来计算。
因此，可以用 np.random 模块去1000次硬币翻转，设置它们为1和-1，并计算累计和
'''

nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()
# 求最大最小值
print(walk.min())
print(walk.max())
# 首次穿越时间，即随机漫步过程中第一次到达某个特定值的时间。
# (np.abs(walk) >= 10 可以得到一个布尔型数组，表示距离是否超过10。
print((np.abs(walk) >= 10).argmax())
# argmax并不是很高效，因为其无论如何都会对数组进行完全扫描。

print('\n一次模拟多个随机漫步\n')
# 如果模拟u多个随机漫步（如5000），只要给numpy.random的函数传入一个二元元组
# 即可产生二维数组。

nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
print(walks)
# 求最大最小值
print(walks.max())
print(walks.min())

# 计算30或-30的最小穿越时间。
# 并不是5000个过程都到达30,所以用any方法检查。
hits30 = (np.abs(walks) >= 30).any(1)

print(hits30)
print(hits30.sum())
# 利用这个布尔数组选出穿越了30的随机漫步，并调用argmax在轴1上获取穿越时间
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
print(crossing_times.mean())

# 其他分布方式得到漫步数据。 如normal用于生成指定均值和标准差的正态分布
steps = np.random.normal(loc=0, scale=0.25, size=(nwalks, nsteps))













