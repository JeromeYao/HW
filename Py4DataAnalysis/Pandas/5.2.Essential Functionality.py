#!/usr/bin/env python3
# Filename:5.2. Essential Functionality.py

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

__author__ = 'JeromeYao'

'''
this's a note of <Python for Data Analysis> -- Wes McKinney
'''

# 本节主要介绍操作Series和DataFrame中的数据的基本手段。

print('\n5.2.1.重新索引\n')
# pandas对象的一个重要方法是reindex，其作用是创建一个适应新索引的新对象。

obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)
'''
Out:
d    4.5
b    7.2
a   -5.3
c    3.6
dtype: float64
'''

# 调用Series的reindex将会根据新索引来重排。
# 如果某个索引值当前不存在，就引入缺失值。

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)
'''
Out:
a   -5.3
b    7.2
c    3.6
d    4.5
e    NaN
dtype: float64
'''
# fill_value参数可以自动为i填入指定缺失值
print(obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0))
'''
Out:
a   -5.3
b    7.2
c    3.6
d    4.5
e    0.0
dtype: float64
'''
# 为了对时间序列这样的数据排序，当重建索引的时候可能想要对值进行内插或填充。
# method 选项可以做到这点，使用一个如 ffill 的方法来向前填充值：

obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)
'''
Out:
0      blue
2    purple
4    yellow
dtype: object
'''
print(obj3.reindex(range(6), method='ffill'))
'''
Out:
0      blue
1      blue
2    purple
3    purple
4    yellow
5    yellow
dtype: object
'''

# 向前向后填充插值
'''
reindex的插值method选项
ffill或pad  前向填充（或搬运）值
bfill或backfill  后向填充（或搬运）值
'''

# 对于DataFrame，reindex可以修改（行）索引、列，或两个都修改。
frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
print(frame)
'''
Out:
   Ohio  Texas  California
a     0      1           2
c     3      4           5
d     6      7           8
'''
# 如果仅传入一个序列，则会重新索引行
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)
'''
Out:
   Ohio  Texas  California
a   0.0    1.0         2.0
b   NaN    NaN         NaN
c   3.0    4.0         5.0
d   6.0    7.0         8.0
'''
# 使用 columns 关键字可以是列重新索引：
states = ['Texas', 'Utah', 'California']
print(frame.reindex(columns=states))
'''
Out:
   Texas  Utah  California
a      1   NaN           2
c      4   NaN           5
d      7   NaN           8
'''
# 可以同时对行列对重新索引，可是插值只在行侧（轴0）进行
# print(frame.reindex(index=['a', 'b', 'c', 'd'], columns=states, method='ffill'))

# 利用ix的标签索引功能，重新索引任务可以变得更加简洁
print(frame.ix[['a', 'b', 'c', 'd'], states])
'''
Out:
   Texas  Utah  California
a    1.0   NaN         2.0
b    NaN   NaN         NaN
c    4.0   NaN         5.0
d    7.0   NaN         8.0
'''

'''
reindex函数的参数
参数  说明
index 用作索引的新序列。既可以是Index实例，也可以是其他序列型的Python数据结构。
method  插值（填充）方式
fill_value  在重新索引的过程中，需要引入缺失值
limit  前向或后向填充时的最大填充量
level  在MultiIndex的指定级别上匹配简单索引，否则选取其子集
copy  默认为True，无论如何都复制;如果为False，则新旧相等就不复制
'''
print(frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill', copy=False))
print('\n5.2.2.丢弃指定轴上的项\n')
# 丢弃某条轴上的一个或多个项很简单，只要有一个索引数组或列表即可。
# 由于需要执行一些数据整理和集合逻辑，所以drop方法返回的是一个在指定轴上删除了指定值的新对象。
obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
print(new_obj)
print(obj.drop(['c', 'd']))

# 对于DataFrame，可以删除任意轴上的索引值
data = DataFrame(np.arange(16).reshape(4, 4),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
print(data, data.drop(['Colorado', 'Ohio']),
      data.drop('two', axis=1), data.drop(['two', 'four'], axis=1),
      '', sep='\n')

print('\n5.2.3.索引、选取和过滤\n')
# Series索引（obj[...]）的工作方式类似于NumPy数组的索引，只不过Series的索引值不是整数
obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj['b'], obj[1], obj[2: 4], obj[['b', 'a', 'd']], obj[[1, 3]], obj[obj <2], sep='\n')

# 利用标签的切片运算与普通的Python切片运算不同，其末端是包含的
print(obj['b': 'c'])
obj['b', 'c'] = 5
print(obj)

# 对DataFrame进行索引其实就是获取一个或多个列
data = DataFrame(np.arange(16).reshape(4, 4),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
print(data, data['two'], data[['three', 'one']], sep='\n')

# 这种索引方式有几个特殊的情况，首先通过切片或布尔类型数组选取行
print(data[:2], data[data['three'] > 5], sep='\n')

# 另一种用法是通过布尔型DataFrame进行索引
print(data < 5)
data[data < 5] = 0
print(data)
# 这段代码的目的是使得DataFrame在语法上更像ndarray。 P131










