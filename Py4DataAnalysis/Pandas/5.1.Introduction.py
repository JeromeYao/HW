#!/usr/bin/env python3
# Filename:5.1. Introduction to pandas Data Structures.py

from pandas import Series, DataFrame
import numpy as np
import  pandas as pd

__author__ = 'JeromeYao'

'''
this's a note of <Python for Data Analysis> -- Wes McKinney
'''


print('\n5.1.Introduction to pandas Data Structures\n')

# pandas重要的数据结构：series 和 DataFrame

print('\n5.1.1. Series\n')
# eries是一个一维的类似的数组对象，包含一个数组的数据
# （任何NumPy的数据类型）和一个与数组关联的数据标签，被叫做索引

obj = Series([4, 7, -5, 3])
print(obj, end='\n\n')

# 索引在左边，值在右边。通过value和index属性获取其数组表示形式和索引对象

print(obj.values, obj.index, sep='\n\n')

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2.index)

# 通过索引的方式选取Series中的单个或一组值。

print(obj2['a'], obj2['d'], obj2[['c', 'a', 'd']], '', sep='\n')

# NumPy数组运算（如根据布尔型数组进行过滤、标量乘法，应用数学函数等）
# 均会保留索引与值之间的链接
print(obj2[obj2 > 0], obj2 * 2, np.exp(obj2), '', sep='\n')

# 还可以将Series看成是一个定长的有序字典，因为它是索引值到数据值的一个映射。
# 可以用在许多原本需要字典参数的函数
print('b' in obj2)
print('e' in obj2, '\n')

# 如果数据被存放在一个Python字典中，也可以直接通过这个字典创建Series：

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
print(obj3, end='\n\n')

# 如果只传入一个字典，则结果Series中的索引就是原字典的键

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
print(obj4, end='\n\n')

# 在这个例子中，sdata中跟states索引相匹配的那3个值会被找出来并放到相应的位置上，
# pandas的isnull和notnull函数可用于检测缺失数据

print(pd.isnull(obj4), end='\n\n')
print(pd.notnull(obj4), end='\n\n')
print(obj4.isnull(), end='\n\n')

# Series最重要的是在算术运算中自动补齐不同索引的数据。
print(obj3, obj4, obj3 + obj4, '', sep='\n')

# Series对象本身及其索引都有一个name属性，该属性跟pandas其他的关键功能关系非常密切

obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)

# Series的索引可以通过赋值的方式就地修改：

obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)

print('\n5.1.2.DataFrame\n')

# DataFrame是一个表格型数据结构，它包含有一组有序的列，每列可以是不同的值类型。
# DataFrame既有行索引也有列索引，可被看成由Series组成的字典。
# 构建DataFrame的方法有很多，最常用的一种是直接传入一个由等长列表或NumPy数组组成的字典。

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print(frame)
# 结果会自动加上索引。
print(DataFrame(data, columns=['year', 'state', 'pop']))
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
print(frame2, end='\n\n')
print(frame2.columns, end='\n\n')

# 和Series一样，在DataFrame中的一列可以通过字典记法或属性来检索

print(frame2['state'], frame2.year, '', sep='\n')

# 返回的Series包含和DataFrame相同的索引，并它们的 name 属性也被正确的设置了。
# 行也可以使用一些方法通过位置或名字来检索，例如 ix 索引成员

print(frame2.ix['three'], end='\n\n')

# 列可以通过赋值来修改。例如，空的 ‘debt’ 列可以通过一个纯量或一个数组来赋值.
frame2['debt'] = 16.5
print(frame2, end='\n\n')
frame2['debt'] = np.arange(5.)
print(frame2, end='\n\n')

# 通过列表或数组给一列赋值时，所赋的值的长度必须和DataFrame的长度相匹配。
# 如果你使用Series来赋值，它会代替在DataFrame中精确匹配的索引的值，并在所有的空位插入丢失数据。

val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2, end='\n\n')

# 给一个不存在的列赋值，将会创建一个新的列。 像字典一样 del 关键字将会删除列

frame2['eastern'] = frame2.state == 'Ohio'
print(frame2, end='\n\n')
del frame2['eastern']
print(frame2.columns)

# 索引DataFrame时返回的列是底层数据的一个视图，而不是一个拷贝。
# 因此，任何在Series上的就地修改都会影响DataFrame。
# 可以使用Series的 copy 函数来显式的拷贝。

# 另一种通用的数据形式是一个嵌套的字典的字典格式：

pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = DataFrame(pop)
print(frame3, frame3.T, '', sep='\n')

# 内层字典的键会被合并，排序以形成最终的索引。
# 如果显示指定了索引,如果显示指定了索引，则不会这样

print(DataFrame(pop, index=[2001, 2002, 2003]), end='\n\n')

# 由Series组成的字典差不多也是一样的用法

pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}
print(DataFrame(pdata), end='\n\n')

'''
可以输入给DataFrame构造器的数据
二维ndarray  数据矩阵，还可以传入行标和列标
由数组、列表或元组构成的字典  每个序列会变成DataFrame的一列。所有序列的长度必须相同
NumPy的结构化/记录数组  类似于‘由数组组成的字典
由Series组成的字典  每个Series会成为一列。如果没有显式指定索引，则各Series的索引会被合并成结果的行索引
由字典组成的字典  各内层字典会成为一列。键会被合并成结果的行索引，跟“由Series组成的字典”的情况一样
字典或Series的列表  各项将会成为DataFrame的一行。字典键或Series索引的并集将会成为DataFrame的列标
列表或元组的列表	和“二维ndarray”一样处理
另一个DataFrame	DataFrame的索引将被使用，除非传递另外一个
NumPy伪装数组（MaskedArray）	除了蒙蔽值在DataFrame中成为NA/丢失数据之外，其它的和“二维ndarray”一样
'''

# 如果设置了DataFrame的index和colums的name属性，则这些信息也会被显示出来
frame3.index.name = 'year'; frame3.columns.name = 'state'
print(frame3, end='\n\n')

# 跟Series一样，values属性也会以二维ndarray的形式返回DataFrame的形式返回DataFrame中的数据
print(frame3.values, end='\n\n')

# 如果DataFrame各列的数据类型不同，则数组的数据类型就会选用能兼容所有列的数据类型
print(frame2.values, end='\n\n')

print('\n2.1.3.Index Object\n')

# pandas的索引对象用来保存坐标轴标签和其它元数据（如坐标轴名或名称）。
# 构建一个Series或DataFrame时任何数组或其它序列标签在内部转化为索引。

obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index, end='\n\n')
print(index[1:], end='\n\n')

# Index对象不可修改，因此用户不能对其进行修改
'''
index[1] = 'd'

Traceback (most recent call last):
    index[1] = 'd'
    raise TypeError("Index does not support mutable operations")
TypeError: Index does not support mutable operations
'''
# 不可修改性非常重要，因为这样才能使Index对象在多个数据结构之间安全共享

index = pd.Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index=index)
print(obj2.index is index, end='\n\n')

'''
pandas中主要的index对象

Index  最泛化的Index对象，将轴标签表示为一个由Python对象组成的NumPy数组
Int64Index  针对整数的特殊Index
MultiIndex  “层次化”索引对象，表示单个轴上的多层索引。可以看做元组组成的数组。
DatetimeIndex  存储纳秒级时间戳（用NumPy的datetime64类型表示）
PeriodIndex  针对Period数据（时间间隔）的特殊Index
'''

# 除了长得像数组，Index的功能也类似一个固定大小额集合
print(frame3, end='\n\n')
print('Ohio' in frame3.columns, 2003 in frame3.index, '', sep='\n')

# 每个索引都有一些方法和属性，它们可以用于设置逻辑并回答有关该索引所包含的数据常见问题。

'''
Index的方法和属性
append  连接另一个Index对象，产生一个新的Index
diff  计算差集，并得到一个Index
intersection  计算交集
union  计算并集
isiin  计算
'''



