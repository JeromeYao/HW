#!/usr/bin/env python3
# Filename:NOP3C_C02_P12.py

__author__ = 'JeromeYao'


print('\n2.12 审查清理文本字符串\n')
'''
Q:文本中混入奇怪的东西，比如：”pýtĥöñ”，如何清理？
'''

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}
a = s.translate(remap)

print(a)

# 删除所有和音符
import unicodedata
import sys


cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))

# 上面例子中,通过使用 dict.fromkeys() 方法构造一个字典,
# 每个 Unicode 和音符作为键,对于的值全部为 None 。
# 然后使用 unicodedata.normalize() 将原始输入标准化为分解形式字符。
# 然后再调用 translate 函数删除所有重音符。
# 同样的技术也可以被用来删除其他类型的字符(比如控制字符等)。
# 构造一个将所有 Unicode 数字字符映射到对应的 ASCII 字符上的表格。

digitmap = {
    c: ord('0') + unicodedata.digit(chr(c))
    for c in range(sys.maxunicode)
    if unicodedata.category(chr(c)) == 'Nd'
}
print(len(digitmap))

# Arabic digits
x = '\u0661\u0662\u0663'

print(x.translate(digitmap))

# 另一种清理文本的技术涉及到 I/O 解码与编码函数。
# 这里的思路是先对文本做一些初步的清理,然后再结合 encode()
# 或者 decode() 操作来清除或修改它。

print(a)
