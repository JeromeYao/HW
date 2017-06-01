#!/usr/bin/env python3
# Filename:NOP3C_C02_P08.py

import re

__author__ = 'JeromeYao'

'''
It's a note of 8th paragraph of 2nd chapter of python3-cookbook chinese version.
'''

print('\n2.8 多行匹配模式\n')

'''
Q:使用正则表达式匹配一大快的文本，需跨多行匹配
'''

comment = re.compile(r'/\*(.*?)\*/')

text1 = '/* this is a comment */'

text2 = '''/* this is a 
multiline comment */
'''

print(comment.findall(text1))

print(comment.findall(text2))

# 修改模式字符串，增加对换行的支持

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

'''
re.compile() 函数接受一个标志参数叫 re.DOTALL ,在这里非常有用。
它可以让正则表达式中的点 (.) 匹配包括换行符在内的任意字符。
'''

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))

'''
对于简单的情况使用 re.DOTALL 标记参数工作的很好,但是如果模式非常复杂或
者是为了构造字符串令牌而将多个模式合并起来 (2.18 节有详细描述),这时候使用这
个标记参数就可能出现一些问题。如果让你选择的话,最好还是定义自己的正则表达
式模式,这样它可以在不需要额外的标记参数下也能工作的很好。
'''
