#!/usr/bin/env python3
# Filename:NOP3C_C02_P01.py

__author__ = 'JeromeYao'

'''
It's a note of 1st paragraph of 2nd chapter of python3-cookbook chinese version
https://github.com/JeromeYao/python3-cookbook/blob/master/source/c02/p01_split_string_on_multiple_delimiters.rst
'''

print('\n2.1 使用多个界定符分割字符串\n')

'''
Q:你需要将一个字符串分割为多个字段，但是分隔符(还有周围的空格)并不是固定的。
'''

# string 对象的 split() 方法只适应于非常简单的字符串分割情形， 它并不允许有多个分隔符或者是分隔符周围不确定的空格。
# 当你需要更加灵活的切割字符串的时候，最好使用 re.split() 方法：

line = 'asdf fjdk; afed, fjek,asdf, foo'
