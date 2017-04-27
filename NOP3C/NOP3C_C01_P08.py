#!/usr/bin/env python3
# Filename:NOP3C_C01_P08.py

'''
It's a note of 8th paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/JeromeYao/python3-cookbook/blob/master/source/c01/p08_calculating_with_dict.rst
'''

__author__ = 'JeromeYao'

print('\n1.8 字典的运算\n')
'''
Q:怎样在数据字典中执行一些计算操作(比如求最小值、最大值、排序等等)？
'''

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# 对字典值操作通常使用zip()函数将键值反转。

min_price = min(zip(prices.values(), prices.keys()))
print('min_price is ', min_price)
max_price = max(zip(prices.values(), prices.keys()))
print('max_price is ', max_price)

# 用zip()和sorted()函数来排列字典数据：

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print('prices_sorted is',prices_sorted)

# zip()函数创建的迭代器只能访问一次。

prices_and_names = zip(prices.values(),prices.keys())
print(min(prices_and_names))
'''
print(max(prices_and_names)) # ValueError: max() arg is an empty sequence
'''
print('\n')

# 如果在一个字典上执行普通的数学运算，仅作用在键。
print(min(prices))
print(max(prices))

# 若使用字典的values()方法 仍不是你想要的结果
print(min(prices.values()))
print(max(prices.values()))

# 使用max()和min()函数中的key参数。
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))

# 若想要查看对应的值，还需执行一次查找。
min_value = prices[min(prices, key=lambda k: prices[k])]

'''
前面的 zip() 函数方案通过将字典"反转"为(值，键)元组序列来解决了上述问题。 
当比较两个元组的时候，值会先进行比较，然后才是键。 
这样的话你就能通过一条简单的语句就能很轻松的实现在字典上的求最值和排序操作了。
'''
# 值相同时，键决定返回值。

prices = {'AAA': 45.23, 'ZZZ': 45.23}
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))