#!/usr/bin/env python3
# Filename:4.5. Linear Algebra.py

__author__ = 'JeromeYao'

'''
this's a note of <Python for Data Analysis> -- Wes McKinney
'''
print('\n4.5. Linear Algebra\n')

import numpy as np
# 线性代数，如矩阵乘法，分解，行列式和其它的方阵数学，对任何一个数组库来说都是重要的部分.
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(x.dot(y))  # x.dot(y) 等同于 np.dot(x, y)
# 在一个二维数组和合适大小的一维数组间的矩阵乘积的结果是一个一维数组
print(np.dot(x, np.ones(3)))
# numpy.linalg 有一个关于矩阵分解和像转置和行列式等的一个标准集合。
from numpy.linalg import inv, qr

X = np.random.randn(5, 5)
mat = X.T.dot(X)
print(inv(mat), end='\n\n')

print(mat.dot(inv(mat)), end='\n\n')

q, r = qr(mat)
print(r)
'''
常用的numpy.linalg函数
diag  以一维数组的形式返回方阵的对角线（或非对角线）元素，或将一维数组转换为方阵（非对角线元素为0）
dot  矩阵乘法
trace  计算对角线元素的和
det  计算矩阵行列式
eig  计算方阵的本征值和本征向量
inv  计算h方阵的逆
pinv  计算矩阵的Moore-Penrose伪逆
qr  计算QR分解,如果实（复）非奇异矩阵A能够化成正交（酉）矩阵Q与实（复）非奇异上三角矩阵R的乘积，即A=QR，则称其为A的QR分解。
svd  计算奇异值分解（SVD）
solve  解线性方程组Ax=b，其中A为一个方阵
lstsq  计算Ax=b的最小二乘解  Compute the least-squares solution to y = Xb
'''






























