#!/usr/bin/env python3
# Filename:NOP3C_C01_P12.py

'''
It's a note of 12th paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/JeromeYao/python3-cookbook/blob/master/source/c01/p12_determine_most_freqently_items_in_seq.rst
'''

__author__ = 'JeromeYao'

print('\n1.12 序列中出现次数最多的元素\n')

'''
Q:怎样找出一个序列中出现次数最多的元素？
'''

# collections.counter 为此而生，其中 most_common()直接可以得到答案。

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]

