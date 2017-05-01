#!/usr/bin/env python3
# Filename:NOP3C_C01_P16.py

'''
It's a note of 16th paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/JeromeYao/python3-cookbook/blob/master/source/c01/p16_filter_sequence_elements.rst
'''

__author__ = 'JeromeYao'

print('\n1.16 过滤序列元素\n')

'''
Q:你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
'''

# 最简单的方法列表推导
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

# 使用列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结果集，占用大量内存。
# 如果你对内存比较敏感，那么你可以使用生成器表达式迭代产生过滤的元素。

pos = (n for n in mylist if n > 0)
print(pos)

for x in pos:
    print(x)

# 有时候，过滤规则比较复杂，不能简单的在列表推导或者生成器表达式中表达出来。
# 比如，假设过滤的时候要处理一些异常或者其他状况。

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)

# filter()函数创建了一个迭代器，因此如果你想得到一个列表的话，就得像示例那样使用list（）去转换。

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math
print([math.sqrt(n) for n in mylist if n > 0])

# 过滤操作的一个变种就是将不符合条件的值用新的值代替，而不是丢弃它们。
# 比如在一列表中你可能不仅想得到正数，而且还想将不是正数的数替代成指定的数。

clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
clip_neg = [n if n < 0 else 0 for n in mylist]
print(clip_neg)

# itertools.compress(), 它以一个 iterable对象和一个相对应的 boolean 选择器序列作为输入参数。
# 然后输出 iterable 对象中对应选择器为True的元素。

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

# 现在你想将那些对应count 值大于5的地址全部输出，那么你可以这样做：

from itertools import  compress
more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(addresses, more5)))

# 这里的关键点在于先创建一个 Boolean 序列，指示哪些元素符合条件。
# 然后 compress() 函数根据这个序列去选择输出对应位置为 True 的元素。

# 和 filter() 函数类似， compress() 也是返回的一个迭代器。
# 因此，如果你需要得到一个列表， 那么你需要使用 list() 来将结果转换为列表类型。
