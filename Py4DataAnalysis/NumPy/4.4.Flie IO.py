#!/usr/bin/env python3
# Filename:4.4. File Input and Output with Arrays.py

__author__ = 'JeromeYao'

'''
this's a note of <Python for Data Analysis> -- Wes McKinney
'''

# NumPy能够保存数据到磁盘和从磁盘加载数据，不论数据是文本或二进制的。

print('\n4.4.1. 对磁盘上的二进制格式数组排序\n')

# np.save和np.load是两个主要函数。
# 默认情况，数组是以未压缩的原始二进制格式保存在扩展名为.npy的文件中。
import numpy as np
arr = np.arange(10)
np.save('some_array', arr)
print(np.load('some_array.npy'))

# 你可以使用 np.savez 并以关键字参数传递数组来保存多个数组到一个zip的归档文件中
np.savez('array_archive.npz', a=arr, b=arr)
arch = np.load('array_archive.npz')
print(arch['b'])

print('\n4.4.2.存取文本文件\n')

# pandas的 read_csv 和 read_table 函数加载文件
# np.loadtxt 或更专门的 np.genfromtxt 对于加载数据到 vanilla NumPy 数组

# 在控制器中输入 !cat array_ex.txt
arr = np.loadtxt('array_ex.txt', delimiter=',')
print(arr)

# np.savatxt 执行相反的操作：写入数组到一个界定文本文件中。
# genfromtxt 与 loadtxt 相似，但是它是面向结构数组和缺失数据处理的
















