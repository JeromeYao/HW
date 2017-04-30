#!/usr/bin/env python3
# Filename:NOP3C_C01_P18.py

'''
It's a note of 18th paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/JeromeYao/python3-cookbook/blob/master/source/c01/p18_map_names_to_sequence_elements.rst
'''

__author__ = 'JeromeYao'

print('\n1.18 映射名称到序列元素\n')

'''
Q:你有一段通过下标访问列表或者元组中元素的代码，但是这样有时候会使得你的代码难以阅读， 如何通过名称来访问元素。
'''

# collections.namedtuple()函数通过使用一个普通的元组对象来帮你解决这个问题。
# 这个函数实际上是一个返回Python中标准元组类型子类的一个工厂方法。
# 你需要传递一个类型名和你需要的字段给它，然后它就会返回一个类，你可以初始化这个类，为你定义的字段传递值等。

from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)


# 使用普通元组的代码


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

# 下标操作通常会让代码表意不清晰，并且非常依赖记录的结构。
# 下面是使用命名元组的版本：

from collections import namedtuple

Stock = namedtuple('Stack', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.share * s.price
    return total

# 命名元组另一个用途就是作为字典的替代，因为字典存储需要更多的内存。
# 如果你需要构建一个非常大的包含字典的数据结构，那么使用命名元组会更加高效。
# 但是需要注意的是，不像字典那样，一个命名元组是不可更改的。

s = Stock('ACME', 100, 123.45)
print(s)

Stock(name='ACME', shares=100, price=123.45)

# _replace()方法还有一个很有用的特性就是当你的命名元组拥有可选或者缺失字段时候，
# 它是一个非常方便的填充数据的方法。
# 你可以先创建一个包含缺省值的原型元组，然后使用 _replace()方法创建新的值被更新过的实例。

from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

# Function to convert a dictionary to a Stock


def dict_to_stock(s):
    return stock_prototype._replace(**s)

# 使用方法：

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012' }
print(dict_to_stock(b))

# 最后要说的是，如果你的目标是定义一个需要更新很多实例属性的高效数据结构，那么命名元组并不是你的最佳选择。
# 这时候你应该考虑定义一个包含 __slots__ 方法的类
