#!/usr/bin/env python3
# Filename:4.1. The NumPy ndarray.py

__author__ = 'JeromeYao'

'''
this's a note of <Python for Data Analysis> -- Wes McKinney
'''

print('\n4.1. NumPy ndarray：多维数组对象\n')

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
ones, ones_like  根据提供的shape和dtype产生一个全1的数组。ones_like用另一个数组作为参数，产生一个shape和dtype都相同的数组。
zeros, zeros_like  同上，但是生成全0的数组
empty,empty_like  通过分配内存来构造新的数组，但不同于ones 和 zeros， 无初值。
eye, identity  生成一个NxN的单位方阵（对角线上为1,其他地方为0）
'''

print('\n4.1.2.ndarray的数据类型\n')

# 数据类型或dtype是一个特别的对象，保存了ndarray如何解释一块内存为特定类型数据的信息。

arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
print('arr1.dtype:', arr1.dtype, 'arr2.dtype:', arr2.dtype)  # Out: arr1.dtype: float64 arr2.dtype: int32

# Dtypes是使NumPy如此强大和灵活的一部分。在大多数情况下，它们直接映射到底层的机器表示，
# 这使得很容易地读取和写入二进制流到磁盘上，也能链接低级语言，如C或Fortran编写的代码。
# 数值表示的dtypes以相同的方式命名：一个类型名，如 folt 或 int ，后面跟着一个表示数字有多少位的数字。
# 一个标准的双精度浮点值（它是Python的 float 对象的底层表示）占据8字节或64位。因此，这一类型在NumPy中被认为是 float64 。

'''
NumPy 数据类型

int8,uint8  有符号和无符号8位（一字节）整数类型
int16,uint16  有符号和无符号16位整数类型
int32,uint32  有符号和无符号32位整数类型
int64,uint64  有符号和无符号64位整数类型
float16  半精度浮点类型
float32  标准精度浮点。与C的float对象兼容
float64,float128  标准双精度浮点。与C的double、Python的float对象兼容
float128  扩展精度浮点
complex64,complex128,complex256  分别使用两个32, 64, 128位浮点表示的复数
bool  布尔值，存储True和False
object  Python对象类型
string_  定长字符串类型（每字符一个字节）。例如，为了生成长度为10的字符串，使用'S10'
unicode_  扩展精度浮点（字节书依赖平台）。同string_有相同的语义规范。
'''

# 你可以使用ndarray的 astype 方法显示的把一个数组的dtype转换或 投射 到另外的类型：

arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)  # Out: int64
float_arr = arr.astype(np.float64)
print(float_arr.dtype)  # Out: float64

# 若浮点数转换到整形dtype，小数将会被截断：

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr)  # Out: [  3.7  -1.2  -2.6   0.5  12.9  10.1]
print(arr.astype(np.int32))  # Out: [ 3 -1 -2  0 12 10]

# astype可以把字符串组转换到数字形式：

numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
print(numeric_strings.astype(float))  # Out: [  1.25  -9.6   42.  ]

# 如果因为某些原因（如一个字符窜不能转换到 float64 ）转换失败了，
# 将会引起一个 TypeError
# 使用 float 而不是 np.float64 ；NumPy会足够聪明的把Python的类型对应到等价的dtypes。
#  你也可以使用dtype的另一个属性：

int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
print(int_array.astype(calibers.dtype))  # Out: [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9.]

# 你也可以使用速记的类型码字符串来指定一个dtype：

empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32)  # Out: [         0 1075314688          0 1075707904          0 107583897          0 1072693248]
print(empty_uint32.shape)  # Out: (8,)

# 调用 astype 总是会创建一个新的数组（原数据的拷贝），即使是新的dtype和原来的dtype相同。

# 值得牢记的是浮点数，如那些是 float64 和 float32 的数组，是唯一能够接近分数的。
# 在复杂的计算中，可能会产生 浮点错误 ，计较时到了一定的小数位数时才有效。

print('\n4.1.3. 数组和纯量间的操作\n')

# 数组的矢量化特性能使你不做循环就可对数据进行操作。
# 相同大小的数组间的算术运算，其操作作用在对应的元素上：

arr = np.array([[1., 2., 3.], [4., 5., 6.]])

print(arr*arr, '\n', arr-arr)
'''
Out:
[[  1.   4.   9.]
 [ 16.  25.  36.]] 
 [[ 0.  0.  0.]
 [ 0.  0.  0.]]
'''

# 纯量操作正如你期望的一样，把操作值用于每一个元素：

print(1/arr, '\n', arr*0.5)
'''
Out:
[[ 1.          0.5         0.33333333]
 [ 0.25        0.2         0.16666667]] 
 [[ 0.5  1.   1.5]
 [ 2.   2.5  3. ]]
'''

# 在不同大小的数组间的操作叫做 broadcasting.

print('\n1.1.4. 基本的索引和切片\n')

# NumPy的索引是一个内容丰富的主题，因为有许多方法可以使你在你的数据中选取一个子集或单个元素。
# 一维的数组很简单，表面上它们的行为类似于Python的列表：

arr = np.arange(10)
print(arr)  # Out: [0 1 2 3 4 5 6 7 8 9]
print(arr[5])  # Out: 5
print(arr[5: 8])  # Out: [5 6 7]
arr[5: 8] = 12
print(arr)  # Out: [ 0  1  2  3  4 12 12 12  8  9]

# 如你所见，当你给一个切片赋一纯量值，如 arr[5:8] = 12 所示，
# 该值被传送（或 传播 ）到整个选择区域。
# 与列表的第一个重要的区别是数组的切片在原来的数组上（不生成新的数组）。
# 这意味着数据不会被拷贝，且对切片的任何修改都会影响源数组：

arr_slice = arr[5: 8]
arr_slice[1] = 12345
print(arr)  # Out: [    0     1     2     3     4    12 12345    12     8     9]

arr_slice[:] = 64
print(arr)  # Out: [ 0  1  2  3  4 64 64 64  8  9]

# 对于高维数组，你会有更多选项。在两维的数组，每一个索引的元素将不再是一个纯量，而是一个一维数组：

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])  # Out: [7 8 9]

# 因此，单个元素可以递归的访问，但是这会做多一点的工作。
# 不过，你可以使用一个逗号分隔的索引列表来选择单个元素。

print(arr2d[0][2])  # Out: 3
print(arr2d[0, 2])  # Out: 3

# 在多维数组中，如果你省略了后面的索引，返回的对象将会是一个较低维的ndarray，
# 它包括较高维度的所有数据。因此，在 2*2*3 的数组 arr3d 中，如下：

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
'''
Out:
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
'''
# arr3d[0] 是一个 2*3 的数组：
print(arr3d[0])
'''
Out:
[[1 2 3]
 [4 5 6]]
'''
# 纯量值和数组都可以给 arr3d[0] 赋值：

old_values = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)
''''
Out:
[[[42 42 42]
  [42 42 42]]

 [[ 7  8  9]
  [10 11 12]]]
'''

arr3d[0] = old_values
print(arr3d)

'''
Out:
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
'''

# 类似的，arr3d[1, 0]给你那些索引以(1, 0)开始的值，形成了一个一维数组：

print(arr3d[1, 0])  # Out: [7 8 9]

# 在所有情况下，被选中的子节返回的数组总是数组视窗。

print('\n1.1.4.1带切片的索引\n')

# 如同一维对象，例如Python的列表，ndarrys可以使用熟悉的语法来切片：

print(arr[1: 6])  # Out: [ 1  2  3  4 64]

# 较高维的对象给你更多的选择，你可以切割一个或多个坐标坐标轴，
# 并且可以混合整数。对上面的2维数组， arr2d ，对它的切片有些不同：

print(arr2d)
'''
Out:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
print(arr2d[:2])
'''
Out:
[[1 2 3]
 [4 5 6]]
'''

# 正如你所见，它沿着0坐标轴切片。因此，一个切片沿着一个坐标轴向选择一个范围额元素。
# 你可以传递多个切片，就像传递多个索引一样：

print(arr2d[:2, 1:])
'''
Out:
[[2 3]
 [5 6]]
'''

# 象这样切片时，你得到的总是相同维数的数组视窗。
# 通过混合整形索引和切片，你可以得到较低维的切片：

print(arr2d[1, :2], '\n', arr2d[2, :1])
'''
Out:
[4 5] 
 [7]
'''

# 一个单一的冒号意味着取整个坐标轴

print(arr2d[:, :1])

'''
Out:
[[1]
 [4]
 [7]]
'''
# 给一个切片表达式赋值会对整个选择赋值：
arr2d[:2, 1:] = 0
print(arr2d)
'''
Out:
[[1 0 0]
 [4 0 0]
 [7 8 9]]
'''

print('\n1.1.5. 布尔索引\n')

# 让我们来考虑一个例子，我们有一些数据在一个数组中和一个有重复名字的数组。
# 我将会在这使用 numpy.random 中的 randn 函数来产生一些随机的正态分布的数据：

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print(names, '\n', data)  # Random out

# 假设每一个名字都和 data 数组中的一行对应。
# 如果我们想要选择与 ‘Bob’ 名字对应的所有行。
# 象算术运算一样，数组的比较操作（例如 == ）也可以矢量化。
# 因此， names 和 Bob 字符窜的比较会产生一个布尔数组：

print(names == 'Bob')  # Out: [ True False False  True False False False]

# 当索引数组时可以传递这一布尔数组：
print(data[names == 'Bob'])  # Random out

# 布尔数组必须和它索引的坐标轴的长度相同。
# 你甚至可以把布尔数组和切片或整数（或者整数序列，
# 关于这一点后面会更多介绍）混合和匹配起来：

print(data[names == 'Bob', 2:])  # Random out
print(data[names == 'Bob', 3])  # Random out

# 选择除Bob以外的所有东西,以下两者等价
print(names != 'Bob')  # Out: [False  True  True False  True  True  True]
print(-(names == 'Bob'), type(-(names == 'Bob')))
# Out: [False  True  True False  True  True  True] <class 'numpy.ndarray'>

# 使用布尔算术操作符如 & （and） 和 | （or）来结合多个布尔条件，下面是从三个名字中选取两个的操作：

mask = (names == 'Bob') | (names == 'Will')  # shouldn't write as: mask = (names == 'Bob') or (names == 'Will')
print(mask)  # Out: [ True False  True  True  True False False]

# 通过布尔索引从一个数组中选取数据，总是会创建数据的一份拷贝，即使返回的数组没有改变。
# Python的 and 和 or 关键字不能和布尔数一起使用。

data[-0.1 < data] = 0  # 使特定元素元素值为特定值
print(data)  # Random out

# 使用一维布尔数组设置整行或列也非常简单：
data[names != 'Joe'] = 7
print(data)  # Random out

print('\n1.1.6. Fancy索引\n')
# Fancy索引是一个术语，被NumPy用来描述使用整形数组索引。
# 假如我们有一个 8*4 的数组：
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i

print(arr)
'''
Out:
[[ 0.  0.  0.  0.]
 [ 1.  1.  1.  1.]
 [ 2.  2.  2.  2.]
 [ 3.  3.  3.  3.]
 [ 4.  4.  4.  4.]
 [ 5.  5.  5.  5.]
 [ 6.  6.  6.  6.]
 [ 7.  7.  7.  7.]]
'''

# 为了选出一个有特定顺序行的子集，
# 你可以传递一个列表或整形ndarray来指定想要的顺序：
print(arr[[4, 3, 0, 6]])
'''
Out:
[[ 4.  4.  4.  4.]
 [ 3.  3.  3.  3.]
 [ 0.  0.  0.  0.]
 [ 6.  6.  6.  6.]]
'''

# 很庆幸这个代码做了你所期望的！
# 使用负的索引从结尾选择行：
print(arr[[-3, -5, -7]])
'''
Out:
[[ 5.  5.  5.  5.]
 [ 3.  3.  3.  3.]
 [ 1.  1.  1.  1.]]
'''

# 传递多个索引数组有些不同；
# 它选取一个一维数组，元素对应与索引的每一个元组：
arr = np.arange(32).reshape((8, 4))
print(arr)
'''
Out:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]
 [24 25 26 27]
 [28 29 30 31]]
'''
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])  # Out: [ 4 23 29 10]

# 花一点儿时间来看看刚刚发生了什么：
# 元素 (1, 0), (5, 3), (7, 1), 和(2, 2)被选择了。
# fancy索引的行为与一些用户可能期望的有所不同，
# 它因该是一个矩形区域，由选取的矩形的行和列组成。
# 这里有一个方法来得到它：
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
'''
Out:
[[ 4  7  5  6]
 [20 23 21 22]
 [28 31 29 30]
 [ 8 11  9 10]]
'''

# 另一种方法是使用 np.ix_ 函数，
# 将两个以为整形数组转换为位标，来选取一个正方形区域：
print(arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
'''
Out:
[[ 4  7  5  6]
 [20 23 21 22]
 [28 31 29 30]
 [ 8 11  9 10]]
'''

# fancy索引，不像切片，它总是拷贝数据到一个新的数组。

print('\n1.1.7. 转置数组和交换坐标轴\n')
# 转置是一种特殊形式的变形，类似的它会返回基础数据的一个视窗，而不会拷贝任何东西。
# 数组有 transpose 方法和专门的 T 属性：
arr = np.arange(15).reshape((3, 5))
print(arr)
'''
Out:
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
'''
print(arr.T)
'''
Out:
[[ 0  5 10]
 [ 1  6 11]
 [ 2  7 12]
 [ 3  8 13]
 [ 4  9 14]]
'''

# 当进行矩阵运算时，你常常会这样做，
# 像下面的例子一样，使用 np.dot 计算内部矩阵来产生 XTX` ：

arr = np.random.randn(6, 3)
print(np.dot(arr.T, arr))  # Random out

# 对于更高维的数组， transpose 接受用于转置的坐标轴的号码的一个元组

arr = np.arange(16).reshape((2, 2, 4))

print(arr)
'''
Out:
[[[ 0  1  2  3]
  [ 4  5  6  7]]

 [[ 8  9 10 11]
  [12 13 14 15]]]
'''
print(arr.transpose((1, 0, 2)))
'''
Out:
[[[ 0  1  2  3]
  [ 8  9 10 11]]

 [[ 4  5  6  7]
  [12 13 14 15]]]
'''

# 使用 .T 的转置，仅仅是交换坐标轴的一个特殊的情况：

print(arr)
'''
Out:
[[[ 0  1  2  3]
  [ 4  5  6  7]]

 [[ 8  9 10 11]
  [12 13 14 15]]]
'''
print(arr.swapaxes(1, 2))
'''
Out:
[[[ 0  4]
  [ 1  5]
  [ 2  6]
  [ 3  7]]

 [[ 8 12]
  [ 9 13]
  [10 14]
  [11 15]]]
'''

# 类似的 swapaxes 返回在数据上的一个视窗，而不进行拷贝。
