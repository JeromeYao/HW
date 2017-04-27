#!/usr/bin/env python3
# Filename:NOP3C_C01_P07.py

'''
It's a note of 7th paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/JeromeYao/python3-cookbook/blob/master/source/c01/p07_keep_dict_in_order.rst
'''

__author__ = 'JeromeYao'

print('\n1.7 字典排序\n')

# 为了能控制一个字典中元素的顺序，你可以使用 collections 模块中的 OrderedDict 类。
# 在迭代操作的时候它会保持元素被插入时的顺序。

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
print(d)
print('\n')

for key in d:
    print(key, d[key])
print('\n')

import json
print(json.dumps(d))

# OrderedDict 内部维护着一个根据键插入顺序排序的双向链8表。
# 每次插入一个新的元素，它会被放到链表的尾部，对于一个已经存在的键的重复值不会改变键的顺序。

# OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。
