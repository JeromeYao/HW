#!/usr/bin/env python3
# Filename:NOP3C_C02_P05.py

__author__ = 'JeromeYao'

'''
It's a note of 5th paragraph of 2nd chapter of python3-cookbook chinese version
https://github.com/JeromeYao/python3-cookbook/blob/master/source/c02/p05_search_and_replace_text.rst
'''

print('\n2.5 字符串搜索和替换\n')

'''
Q:你想在字符串中搜索和匹配指定的文本模式
'''

# 对于简单的字面模式，直接使用 str.repalce() 方法即可，比如：

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

# 对于复杂的模式，请使用 re 模块中的 sub() 函数。
# 为了说明这个，假设你想将形式为 11/27/2012 的日期字符串改成 2012-11-27 。示例如下：

text = 'Today is 11/27/2012.PyCon starts 3/13/2013.'

import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

# sub()函数中的第一个参数是被匹配的模式，第二个参数是替换模式。
# 反斜杠数字比如 \3 指向前面模式的捕获组号。
# 如果你打算用相同的模式做多次替换，考虑先编译它来提升性能。

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

# 对于更加复杂的替换，可以传递一个替换回调函数来代替，比如：

from calendar import month_abbr


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print(datepat.sub(change_date, text))

# 一个替换回调函数的参数是一个 match 对象，也就是 match() 或者 find() 返回的对象。
# 使用 group() 方法来提取特定的匹配部分。回调函数最后返回替换字符串。

# 如果除了替换后的结果外，你还想知道有多少替换发生了，可以使用 re.subn() 来代替。比如：

newtext, n = datepat.subn(r'\3-\1-\2', text)
print('newtext:', newtext, 'n:', n)
