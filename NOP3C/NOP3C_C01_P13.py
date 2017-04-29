#!/usr/bin/env python3
# Filename:NOP3C_C01_P13.py

'''
It's a note of 13th paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/JeromeYao/python3-cookbook/blob/master/source/c01/p13_sort_list_of_dicts_by_key.rst
'''

__author__ = 'JeromeYao'

print('\n1.13 通过某个关键字排序一个字典列表\n')

'''
Q:你有一个字典列表，如何根据某个或某几个字典字段来排序这个列表？
'''

# operator 模块的 itemgetter 函数

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

# 在上面例子中， rows 被传递给接受一个关键字参数的 sorted() 内置函数。
# 这个参数是 callable 类型，并且从 rows 中接受一个单一元素，然后返回被用来排序的值。
# itemgetter() 函数就是负责创建这个 callable 对象的。

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))

print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))

