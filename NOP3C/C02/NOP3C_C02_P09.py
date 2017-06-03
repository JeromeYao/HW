#!/usr/bin/env python3
# Filename:NOP3C_C02_P09.py

__author__ = 'JeromeYao'

print('\n2.09 将Unicode文本标准化\n')

'''
Q:处理Unicode字符串。需要确保所有字符串在底层有相同的表示。
'''

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1, s2, s1 == s2, len(s1), len(s2))

'''
这里的文本”Spicy Jalapeño” 使用了两种形式来表示。第一种使用整体字符”ñ”(U
+00F1),第二种使用拉丁字母”n” 后面跟一个” ̃̃”（可能显示不出） 的组合字符 (U+0303)。
'''

# 在需要比较字符串的程序中使用字符的多种表示会产生问题。
# unicodedata 模块先将文本标准化

import unicodedata

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1, t2, t1 == t2)

print(ascii(t1))
t3, t4 = unicodedata.normalize('NFD', s1), unicodedata.normalize('NFD', s2)
print(t3, t4, t3 == t4)

'''
normalize() 第一个参数指定字符串标准化的方式。
NFC 表示字符应该是整体组成 (比如可能的话就使用单一编码),
而 NFD 表示字符应该分解为多个组合字符表示。
'''

'''
Python 同样支持扩展的标准化形式 NFKC 和 NFKD,它们在处理某些字符的时候
增加了额外的兼容特性。
'''

s = '\ufb01'  # A single character
print(s)

print(unicodedata.normalize('NFD', s))
print(unicodedata.normalize('NFKD', s), unicodedata.normalize('NFKC', s))

'''
标准化对于任何需要以一致的方式处理 Unicode 文本的程序都是非常重要的。
当处理来自用户输入的字符串而你很难去控制编码的时候尤其如此。
在清理和过滤文本的时候字符的标准化也是很重要的。
'''

t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
# combining() 函数可以测试一个字符是否为和音字符
