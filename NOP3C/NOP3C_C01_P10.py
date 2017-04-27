#!/usr/bin/env python3
# Filename:NOP3C_C01_P10.py

'''
It's a note of 10th paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/JeromeYao/python3-cookbook/blob/master/source/c01/p09_find_commonalities_in_dicts.rst
'''

__author__ = 'JeromeYao'

print('\n1.10 删除序列相同元素并保持顺序\n')

'''
Q:怎样在一个序列上面保持元素顺序的同时消除重复的值？
'''

# 如果序列的值都为 hashable 类型，可用集合或生成器解决。


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
        seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))
print('\n')


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        yield item
        seen.add(val)

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))

# 如果单纯想消除重复项，可以构造一个集合，但不能保证顺序。

print(a)
print(set(a))

'''
文件消除重复行，可以这样做

with open(somefile,'r') as f:
for line in dedupe(f):
    pass
'''