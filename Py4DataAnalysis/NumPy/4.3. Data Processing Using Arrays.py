#!/usr/bin/env python3
# Filename:4.3. Data Processing Using Arrays.py

__author__ = 'JeromeYao'

'''
this's a note of <Python for Data Analysis> -- Wes McKinney
'''

# ndarray的矢量化特性使你将多种数据处理表述为简洁的数组表达式，从而避免了循环语句。
# 在一组值上计算sqrt(x^2 + y^2)
import numpy as np
import matplotlib.pyplot as plt
points = np.arange(-5, 5, 0.01)  # 1000个间隔相等的点
xs, ys = np.meshgrid(points, points)
print(ys)
z = np.sqrt(xs**2 + ys**2)
print(z)
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

print('\n4.3.1.将条件逻辑表述为数组运算\n')

# numpy.where 是三元表达式 x if condition else y 的矢量化版本

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result1 = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print(result1)
#
result2 = np.where(cond, xarr, yarr)
print(result2)
#

arr = np.random.randn(4, 4)
print(arr)  # Random out
print(np.where(arr > 0, 2, -2))  # Random out

# 有两个布尔数组， cond1 和 cond2 ，并想根据4种布尔值来赋值：
cond1 = np.array([True, False, False, True, True])
cond2 = np.array([True, True, False, False, True])
result = []
for i in range(len(cond1)):
    if cond1[i] and cond2[i]:
        result.append(0)
    elif cond1[i]:
        result.append(1)
    elif cond2[i]:
        result.append(2)
    else:
        result.append(3)
print(result)  # Out: [0, 2, 3, 1, 0]

# 这个 for 循环可以转换成一个嵌套的 where 表达式：

result = np.where(cond1 & cond2, 0, np.where(cond1, 1, np.where(cond2, 2, 3)))
print(result)  # Out: [0 2 3 1 0]

# 利用布尔表达式在计算中被当作0或1这一事实，因此可以使用算术运算来表达：

result = 1 * cond1 + 2 * cond2 + 3 * -(cond1 | cond2)
print(result)

print('\n4.3.2. 数学和统计方法\n')

# 一组数学函数，计算整个数组或一个轴向上数据的统计，
# 和数组函数一样是容易访问的。聚合（通常被称为 reductions ），
# 如sun， mean，标准偏差 std 可以使用数组实例的方法，
# 也可以使用顶层NumPy的函数

arr = np.random.randn(5, 4)  # 正态分布数据
print(arr.mean())
print(np.mean(arr))
print(arr.sum())

# 像 mean 和 sun 函数可以有一个可选的 axis 参数，
# 它对给定坐标轴进行统计，结果数组将会减少一个维度：

arr.mean(axis=1)  # axis轴，维度的意思
print(np.array([-1.2833, 0.2844, 0.6574, 0.6743, -0.0187]))
print(arr.sum(0))

'''
数组构建函数
sum  对数组的所有或一个轴向上的元素求和。零长度的数组的和为零。
mean  算术平均值。零长度的数组的均值为NaN。
std,var  标准差和方差，有可选的调整自由度（默认值为n）。
min, max  最小指和最大值
argmin, argmax  索引最小元素和最大元素
cumsum  从0元素开始的累计和
cumprod  从1元素开始的累计乘
'''
arr = np.arange(0, 10)
print(np.cumsum(arr), arr.cumsum(), sep='\n')  # 两种输出方式均可。
'''
Out: 
[ 0  1  3  6 10 15 21 28 36 45]
[ 0  1  3  6 10 15 21 28 36 45]
'''
print(sum(arr))  # Out: 45
# 经过对比cumsum和sum可以发现，cumsum即为[sum(d[0]), sum(d[0: 1]), ..., sum(d)]
# cumprod与cumsum机制类似。这些函数并不聚集，而是产生一个 intermediate results 的数组.

print('\n4.3.3. 布尔数组的方法\n')

# 在上面的方法中布尔值被强制为1( True )和0( False )。
# 因此，sum 经常被用来作为对一个布尔数组中的 True 计数的手段：

arr = np.random.randn(100)
print((arr > 0).sum())  # Random Out,求正数个数

# 有两个额外的方法， any 和 all ，
# 对布尔数组尤其有用。 any 用来测试一个数组中是否有一个或更多的 True ，
# 而 all 用来测试所有的值是否为 True ：
bools = np.array([False, False, True, False])
print(bools.any())  # Out: True
print(bools.all())  # Out: False
# 这些方法这些方法也可以工作在非不而数组上，非零元素作为 True 。

print('\n4.3.4. 排序\n')
# 像Python的内建列表一样，NumPy数组也可以使用 sort 方法就地排序
arr = np.random.randn(8)
print(arr)
arr.sort()
print(arr, end='\n\n')

# 多维数组可以通过传递一个坐标轴数到 sort ，
# 对一维截面上的数据进行就地排序

arr = np.random.randn(5, 3, 2)
print('arr:\n', arr, end='\n\n')
arr.sort(1)
print('arr:\n', arr, end='\n\n')
arr.sort(0)
print('arr:\n', arr, end='\n\n')

# 顶层方法np.sort返回的是数组的已排序副本，而就地排序则会修改数组本身。
# 计算数组分组数最简单的办法是对其进行排序，然后选取特定位置的值

large_arr = np.random.randn(1000)
large_arr.sort()
print(large_arr[int(0.05 * len(large_arr))])

print('\n唯一化以及其他的集合逻辑\n')

# Numpy有一些基本的针对一维ndarrays的集合操作。
# 最常使用的一个可能是 np.unique ，
# 它返回一个数组的经过排序的 unique 值

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))  # Out: ['Bob' 'Joe' 'Will']

ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))  # Out: [1 2 3 4]

# 与np.unique对比
print(sorted(set(names)))  # Out: ['Bob', 'Joe', 'Will']

# 另一个函数np.in1d用于测试一个数组中的值在另一个数组中的成员资格
# 返回一个布尔数组

values = np.array(([6, 0, 0, 3, 2, 5, 6]))
print(np.in1d(values, [2, 3, 6]))

'''
数组的集合运算
方法  说明
unique(x)  计算x中的唯一元素，并返回有序结果
intersect1d(x, y)  计算x和y中的公共元素，并返回有序结果
in1d(x, y)  得到一个表示‘x的元素是否包含于y’的布尔数组
setdiff1d(x, y)  集合的差，即元素在x中且不在y中
setxorld(x, y)  对称差集，不同时在两个数组中的元素
'''
















