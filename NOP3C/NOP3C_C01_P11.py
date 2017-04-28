#!/usr/bin/env python3
# Filename:NOP3C_C01_P11.py

'''
It's a note of 11th paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/JeromeYao/python3-cookbook/blob/master/source/c01/p11_naming_slice.rst
'''

__author__ = 'JeromeYao'

print('\n1.11 命名切片\n')

'''
Q:你的程序已经出现一大堆已无法直视的硬编码切片下标，然后你想清理下代码。
'''

# 假定你有一段代码要从一个记录字符串中几个固定位置提取出特定的数据字段(比如文件或类似格式)：
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])

# 更好的方案，使得代码清晰可读

SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])

# 内置的slice()函数创建一个切片对象。

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])
items[a] = [10, 11]
print(items)
del items[a]
print(items)

a = slice(5, 50, 2)
print(a.start)
print(a.stop)
print(a.step)
print('\n')
# 切片的indices(size)方法可以将此方法映射到确定大小的序列上。

s = 'Helloworld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])

