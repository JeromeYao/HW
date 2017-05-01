#!/usr/bin/env python3
# Filename:NOP3C_C01_P17.py

'''
It's a note of 17th paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/JeromeYao/python3-cookbook/blob/master/source/c01/p17_extract_subset_of_dict.rst
'''

__author__ = 'JeromeYao'

print('\n1.17 从字典中提取子集\n')

'''
Q:构造一个字典，它是另外一个字典的子集
'''

# 用字典推导
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 265.55,
    'HPQ': 37.28,
    'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)

# 大多数情况下字典推导能做到的，通过创建一个元组序列然后把它传给dict()函数也能实现。

p1 = dict((key, value) for key, value in prices.items() if calue > 200)

# 但是，字典推导方式表意更清晰，并且实际上也会运行的更快些 (在这个例子中，实际测试几乎比 dcit() 函数方式快整整一倍)。

# 第二个例子也可以像这样重写：

# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: prices[key] for key in prices.keys() & tech_names}

# 但是，运行时间测试结果显示这种方案大概比第一种方案慢1.6倍。
