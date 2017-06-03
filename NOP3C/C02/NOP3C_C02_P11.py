#!\usr\bin\env python
# Filename:NOP3C_C02_P11.py

__author__ = 'JeromeYao'

print('\n2.11删除字符串中不需要的字符\n')

'''
Q:去掉文本字符串开头,结尾或者中间不想要的字符,比如空白。
'''

# strip()方法可以删除开始或结束的字符。
# lstrip()和rstrip()分别从左和右执行删除操作。

# Whitespace stripping

s = ' hello world \n'

print(s.strip(), s.rstrip(), s.lstrip(), sep='**')

# Character stripping

t = '-----hello====='

print(t.lstrip('-'))

print(t.strip('-='))

'''
这些 strip() 方法在读取和清理数据以备后续处理的时候是经常会被用到的。
比如,你可以用它们来去掉空格,引号和完成其他任务。
但是需要注意的是去除操作不会对字符串的中间的文本产生任何影响。
'''

s = ' hello    world \n'
print(s.strip())

# 若处理中间的空格，可用replace()或正则表达式替换
print(s.replace(' ', ''))

import re

print(re.sub('\s+', ' ', s))

'''
通常情况下你想将字符串 strip 操作和其他迭代操作相结合,
比如从文件中读取多行数据。
如果是这样的话,那么生成器表达式就可以大显身手了.

with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)

表达式 lines = (line.strip() for line in f) 执行数据转换操作。
这种方式非常高效,因为它不需要预先读取所有数据放到一个临时的列表中去。
它仅仅只是创建一个生成器,并且每次返回行之前会先执行 strip 操作。
'''