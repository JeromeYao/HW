#!/usr/bin/env python3
# Filename:1.1. NumPy ndarray.py

__author__ = 'JeromeYao'

'''
It's a note of Numpy
http://pda.readthedocs.io/en/latest/chp4.html
'''

print('\n1.1. NumPy ndarray：多维数组对象\n')

# NumPy的一个关键特性是它的N维数组对象(ndarray)
# 一个大型数据集的快速的，灵活的容器
# 数组使你能在整个数据块上进行数学运算，且与对应纯量元素间操作有相似的语法。

import numpy as np

data = np.array(
    [[0.9526, -0.246, -0.8856],
    [0.5639, 0.2379, 0.9104]]
)
print(type(data))  # Out: <class 'numpy.ndarray'>
print(data*10)
'''
Out:
[[ 9.526 -2.46  -8.856]
 [ 5.639  2.379  9.104]]
'''
print(data + data)
'''
Out:
[[ 1.9052 -0.492  -1.7712]
 [ 1.1278  0.4758  1.8208]]
'''
# ndarry是一个同种类数据的多维容器，所有元素都是同类型的。
# 每个数组都有一个shape（表示它的每一维大小的元组）和dtaye（一个描述数组数据类型的对象）

print(data.shape)  # Out: (2, 3)
print(data.dtype)  # Out: float64

'''
'array', 'NumPy array', 'ndarray' 一般均指ndarry对象。
'''

print('\n1.1.1. 创建ndarray\n')

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)  # Out: [ 6.   7.5  8.   0.   1. ]

# 嵌套序列，如等长列表的列表，将会转化为一个多维数组：
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)
'''
Out:
[[1 2 3 4]
 [5 6 7 8]]
'''
print(arr2.ndim)  # Out: 2
print(arr2.shape)  # Out: (2, 4)

# 常用新建数组方法 zeros 和 ones 使用给定的长度或形状创建 0's 和 1's 数组。
# empty 创建一个没有使用特定值来初始化的数组。
# 给这些方法传递一个元组作为形状来创建高位数组：

print(np.zeros(10))  # Out: [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
print(np.zeros((3, 6)))
'''
Out:
[[ 0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.]]
'''
print(np.ones((50, 50)))
'''
Out:
[[ 1.  1.  1. ...,  1.  1.  1.]
 [ 1.  1.  1. ...,  1.  1.  1.]
 [ 1.  1.  1. ...,  1.  1.  1.]
 ..., 
 [ 1.  1.  1. ...,  1.  1.  1.]
 [ 1.  1.  1. ...,  1.  1.  1.]
 [ 1.  1.  1. ...,  1.  1.  1.]]
'''

print(np.empty((2, 3, 2)))

'''
Out:
[[[  6.94621877e-310   1.71478091e-316]
  [  6.94621966e-310   6.94621354e-310]
  [  6.94621961e-310   6.94621783e-310]]

 [[  6.94621970e-310   6.94621966e-310]
  [  6.94621961e-310   6.94621972e-310]
  [  6.94621972e-310   6.94621972e-310]]]
'''

# arange 是 python内建 range 函数的数组版本：

print(np.arange(15))  # Out: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

'''
用于构建数组的标准函数清单：
array  转换输入数据（列表，数组或者其他序列类型）到一个ndarray ，
可以推断一个dtype或明确的设置一个dtype。默认拷贝输入数据。
asarray  转换输入为一个ndarray， 当输入已经是一个ndarray时就不拷贝。
arange  同内建的range函数，但不返回列表而是一个ndarray

'''