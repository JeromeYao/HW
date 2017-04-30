#!/usr/bin/env python3
# Filename:NOP3C_C01_P09.py

'''
It's a note of 9th paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/JeromeYao/python3-cookbook/blob/master/source/c01/p09_find_commonalities_in_dicts.rst
'''

__author__ = 'JeromeYao'

print('\n1.9查找两个字典的相同点\n')

'''
Q:怎样在两个字典中寻找相同点（如键、值）？
'''

a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# 执行集合操作。

print('Find keys in common:', a.keys() & b.keys())
print('Find keys in a that are not in b', a.keys() - b.keys())
print('Find (key, value)pairs in common', a.items() & b.items())

# 可用于修改或过滤字典元素。

print('Make a new dictionary with certain keys removed', {key: a[key] for key in a.keys() - {'z', 'w'}})

'''
字典本质就是一个键集合与一个值集合的映射关系。
字典的keys()方法返回一个展现键集合的键视图对象。键视图支持集合操作，如：交、并、差运算。
items()方法返回一个包含键值对的元素试图对象，同样支持集合操作。
values()方法类似，但不支持集合操作，因为值视图不能保证所有值互不相同。如果要在值上操作可以先将值转换成set。
'''
