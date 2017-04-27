#!/usr/bin/env python3
# Filename:NOP3C_C01_P06.py

'''
It's a note of 6th paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/JeromeYao/python3-cookbook/blob/master/source/c01/p06_map_keys_to_multiple_values_in_dict.rst
'''

__author__ = 'JeromeYao'

print('\n1.6 字典中的键映射多个值\n')

'''
Q:怎样实现一个键对应多个值的字典(也叫 multidict )？
'''
# 一个字典就是一个键对应一个单值的映射。如果要一个键映射多个值，
# 那么需将这多个值放到另外的容器中，比如列表或者集合里面。
# 需保留插入顺序，用列表。需去除重复值则用集合。

d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}

e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}

print(d)
print(e)

# 使用collections 模块中的defaultdict 来构造字典。
# defaultdict的一个特征是它会自动初始化每个key刚开始对应的值。

from collections import defaultdict

d = defaultdict(list)
print(d)
d['a'].append(1)
print(d)
d['a'].append(2)
print(d)
d['b'].append(4)
print(d)
print('\n')

d = defaultdict(set)
print(d)
d['a'].add(1)
print(d)
d['a'].add(2)
print(d)
d['b'].add(4)
print(d)
print('\n')

d = {} # A regular dictionary
print(d)
d.setdefault('a', []).append(1)
print(d)
d.setdefault('a', []).append(2)
print(d)
d.setdefault('b', []).append(4)
print(d)

# 有人可能觉得setdefault()用起来别扭，每次调用都需要创建一个新的初始值实例。

# 自行实现多值映射字典
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
print(d)
# 若使用defaultdict

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
print(d)



