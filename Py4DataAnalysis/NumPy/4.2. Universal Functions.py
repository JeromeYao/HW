#!/usr/bin/env python3
# Filename:4.2. Universal Functions.py

__author__ = 'JeromeYao'

'''
this's a note of <Python for Data Analysis> -- Wes McKinney
'''
import numpy as np
# 许多 ufuncs 都是基于元素的简单变换，像 sqrt 或 exp ：
arr = np.arange(10)
print(np.sqrt(arr))
'''
Out:
[ 0.          1.          1.41421356  1.73205081  2.          2.23606798
  2.44948974  2.64575131  2.82842712  3.        ]
'''
print(np.exp(arr))
'''
Out:
[  1.00000000e+00   2.71828183e+00   7.38905610e+00   2.00855369e+01
   5.45981500e+01   1.48413159e+02   4.03428793e+02   1.09663316e+03
   2.98095799e+03   8.10308393e+03]
'''

# 这些归诸于 unary ufuncs。其它的，例如 add 或 maximum ，
# 接受两个数组（因此，叫做 binary ufuncs）且返回一个数组：

x = np.random.randn(8)
y = np.random.randn(8)
print(x, y, np.maximum(x, y), sep='\n')  # Random out, 输出元素级最大值

# 有些ufunc可以返回多个数组。
# nodf 就是一个例子，它是Python内建 divmod 的矢量化的版本：它返回一个浮点数数组的分数和整数部分
print(np.modf(np.random.randn(7) * 5))  # Random out

'''
----Unary ufuncs----
abs,fabs  计算基于元素的整形，浮点或复数的绝对值。fabs对于没有复数数据的快速版本
sqrt  计算每个元素的平方根。等价于 arr ** 0.5
square  计算每个元素的平方。等价于 arr ** 2
exp  计算每个元素的指数
log, log10, log2, log1p  自然对数（基于e），基于10的对数，基于2的对数和 log(1 + x)
sign  计算每个元素的符号：1(positive)，0(zero)， -1(negative)
ceil  计算每个元素的天花板，即大于或等于每个元素的最小值
floor  计算每个元素的地板，即小于或等于每个元素的最大值
rint  圆整每个元素到最近的整数，保留dtype
modf  分别返回分数和整数部分的数组
isnan  返回布尔数组标识哪些元素是 NaN （不是一个数）
isfinite, isinf  分别返回布尔数组标识哪些元素是有限的（non-inf, non-NaN）或无限的
cos, cosh, sin sinh, tan, tanh  regular 和 hyperbolic 三角函数
arccos, arccosh, arcsin, arcsinh, arctan, arctanh  反三角函数
logical_not  计算基于元素的非x的真值。等价于 -arr
'''

'''
----Binary universal functions----
add  在数组中添加相应的元素
subtract   从第一个数组中减去第二个数组中的元素
multiply 数组元素相乘
divide、floor_divide  除法或向下圆整除（丢弃余数）
power  对地一个数组中的元素A，根据第二个数组中的相应元素B，计算A**B
maximum、fmax  元素级最大值计算。fmax将忽略NaN
minimum、fmin  元素级最小值计算。fmin将忽略NaN
mod  元素级求模计算（除法的余数）
copysign  将第二个数组中的值的符号复制给第一个数组中的值
greater, greater_equal, less, less_equal, not_equal  基于元素的比较，产生布尔数组。等价于中缀操作符 >, >=, <, <=, ==, !=
logical_and, logical_or, logical_xor  计算各个元素逻辑操作的真值。等价于中缀操作符 &, |, ^
'''
