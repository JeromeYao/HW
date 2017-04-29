#!/usr/bin/env python3
# Filename:NOP3C_C01_P14.py

'''
It's a note of 14th paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/JeromeYao/python3-cookbook/blob/master/source/c01/p13_sort_list_of_dicts_by_key.rst
'''

__author__ = 'JeromeYao'

print('\n1.14 排序不支持原生比较的对象\n')

'''
Q:你想排序类型相同的对象，但是他们不支持原生的比较操作。
'''

# 内置的sorted()内涵有一个关键字参数key，可以传入一个callable对象给它，


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'uesr({})'.format(self.user_id)


def sort_notcomqare():
        users = [User(23),  User(3), User(99)]
        print(users)
        print(sorted(users, key=lambda u: u.user_id))

# 另外一种方式是使用 operator.attrgetter() 来代替lambda函数：

'''
from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))
'''

# by_name = sorted(users, key=attrgetter('last_name', 'first_name'))

# print(min(users, key=attrgetter('user_id')))
# print(max(users, key=attrgetter('user_id')))

