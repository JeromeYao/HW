#!/usr/bin/env python3
# Filename:NOP3C_C01_P01.py

'''
It's a note of 1st paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/yidao620c/python3-cookbook/blob/master/source/c01/p01_unpack_sequence_into_separate_variables.rst
'''

__author__ = 'JeromeYao'

print('\n1.1解压序列赋值给多个变量\n')

'''
Q:现在有一个包含N个元素的元组或者是序列，
怎样将它里面的值解压后同时赋值给N个变量？
'''

'''
任何的序列(或者是可迭代对象)可以通过一个简单的赋值语句解压并赋值给多个变量。 
唯一的前提就是变量的数量必须跟序列元素的数量是一样的。
'''

p = (4, 5)
x, y = p
# 元组中的元素指向指定变量，则这写变量
print('x:%s y:%s' % (x, y))

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
# 例如：以上序列data的第0到3个元素分别指向不同变量，使得这些变量可以直接引用序列中的元素。
print('name:%s\nshares:%s\nprice:%s\ndate:%s\ndata:%s' % (name, shares, price, date, data))

year, mon, day = date
# 更多例子
print('year:%s\nmon:%s\nday:%s\n' % (year, mon, day))
'''
注意 若变量个数和序列元素个数不匹配会产生一个异常。
p = (4, 5)
x, y, z = p

Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: need more than 2 values to unpack
'''

# 此方法不仅适用于序列，字符串、文件、迭代器、生成器同样适用。

# 只想解压部分值可以用占位变量，并丢弃不需要的变量。
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_nonsense1, shares, price, _nonsense2 = data
print('shares:%s price:%s\n' % (shares, price))

