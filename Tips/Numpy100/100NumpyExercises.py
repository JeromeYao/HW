#! usr/bin/env python3
# Filename: 100NumpyExercises.py

__author__ = 'Jerome Yao'
'''

'''

# 1. Import the numpy package under the name np (★☆☆)
import numpy as np

# 2. Print the numpy version and the configuration (★☆☆)
print('#2:\n', np.__version__)
np.show_config()  # other way

# 3. Create a null vector of size 10 (★☆☆)
print('#3:\n', np.zeros(10))

# 4. How to find the memory size of any array (★☆☆)
array = np.zeros((10, 10))
print('#4:\n', '%d bytes' % (array.size * array.itemsize))  # 800bytes

# 待解决5. How to get the documentation of the numpy add function from the command line? (★☆☆)  ##
# %run `python -c "import numpy; numpy.info(numpy.add)"`

# 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
vector = np.zeros(10)
vector[4] = 1
print('#6:\n', vector)

# 7. Create a vector with values ranging from 10 to 49 (★☆☆)
vector = np.arange(10, 50)
print('#7:\n', vector)

# 8. Reverse a vector (first element becomes last) (★☆☆)
vector = np.arange(10)
vector1 = list(reversed(vector))
print('#8:\n', vector1)

# 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
matrix = np.arange(9).reshape(3, 3)
print('#9:\n', matrix)

# 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
vector = np.nonzero([1, 2, 0, 0, 4, 0])
print('#10:\n', vector)

# 11. Create a 3x3 identity matrix (★☆☆)
matrix = np.eye(3)
print('#11:\n', matrix)

# 12. Create a 3x3x3 array with random values (★☆☆)
array = np.random.random((3, 3, 3))
print('#12:\n', array)

# 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
array = np.random.random((10, 10))
print('#13:\n', array.max(), array.min())

# 14. Create a random vector of size 30 and find the mean value (★☆☆)
vector = np.random.random(30)
print('#14:\n', vector.mean())

# 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
array = np.ones((7, 7))
array[1:-1, 1:-1] = 0
print('#15:\n', array)

# 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
array = np.ones((5, 5))
array1 = np.zeros((7, 7))
array1[1: -1, 1: -1] = array
print('#16:\n', array1)
# or
array = np.ones((5, 5))
array1 = np.pad(array, pad_width=1, mode='constant', constant_values=0)
print('or:\n', array1)

# 17. What is the result of the following expression? (★☆☆)
'''
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
0.3 == 3 * 0.1
'''
print('#17:\n', end='')
print(0 * np.nan)
print(np.nan == np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1)
print(0.1 * 3)

# 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
matrix = np.diag(1+np.arange(4), k=-1)
print('#18:\n', matrix)

# 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
matrix = np.zeros((8, 8), dtype=int)
matrix[1::2, ::2] = 1
matrix[::2, 1::2] = 1
print('#19:\n', matrix)

# 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
print('#20:\n', np.unravel_index(100, (6, 7, 8)))

# 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)  棋盘展开
matrix = np.tile(np.array([[0, 1], [1, 0]]), (4, 4))
print('#21:\n', matrix)

# 22. Normalize a 5x5 random matrix (★☆☆)  标准化矩阵
m = np.random.random((5, 5))
mmax, mmin = m.max(), m.min()
m = ((m - mmin)/(mmax - mmin))
print('#22:\n', m)

# 待解决23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)
color = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])

# 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
matrix = np.dot(np.ones((5, 3)), np.ones((3, 2)))
print(matrix)

# 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
array = np.arange(11)
array[(array >= 3) & (array <= 8)] *= -1
print(array)

# 26. What is the output of the following script? (★☆☆)
print(sum(range(5), -1))  # 9
print(np.sum(range(5), -1))  # 10

# 待解决27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
'''
Z**Z
2 << Z >> 2
Z <- Z
1j*Z
Z/1/1
Z<Z>Z
'''

# 待解决28. What are the result of the following expressions?
'''
print(np.array(0) / np.array(0))
print(np.array(0) // np.array(0))
print(np.array([np.nan]).astype(int).astype(float))
'''

# 29. How to round away from zero a float array ? (★☆☆)
Z = np.random.uniform(-10, +10, 10)  # numpy.random.uniform(low,high,size)
print(np.copysign(np.ceil(np.abs(Z)), Z))

# 30. How to find common values between two arrays? (★☆☆)
array1 = np.random.randint(0, 10, 10)
array2 = np.random.randint(0, 10, 10)
array = np.intersect1d(array1, array2)  # intersect1d(x, y) 计算x and y 的公共元素
print(array)

# 31. How to ignore all numpy warnings (not recommended)? (★☆☆)

# Suicide mode on
defaults = np.seterr(all="ignore")
Z = np.ones(1) / 0
print(Z)
# Back to sanity
_ = np.seterr(**defaults)

# An equivalent way, with a context manager:
with np.errstate(divide='ignore'):
    Z = np.ones(1) / 0
print(Z)
# Back to sanity
_ = np.seterr(**defaults)

# 32. Is the following expressions true? (★☆☆)
# np.sqrt(-1) == np.emath.sqrt(-1)

# 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print(yesterday, today, tomorrow, sep='\n')

# 34. How to get all the dates corresponding to the month of July 2016? (★★☆)
Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(Z)

# 35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)
A = np.ones(3)*1
B = np.ones(3)*2
C = np.ones(3)*3
np.add(A, B, out=B)
np.divide(A, 2, out=A)
np.negative(A, out=A)
np.multiply(A, B, out=A)

# 36. Extract the integer part of a random array using 5 different methods (★★☆)
Z = np.random.uniform(0, 10, 10)
print(Z - Z % 1)
print(np.floor(Z))
print(np.ceil(Z)-1)
print(Z.astype(int))
print(np.trunc(Z))

# 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)
matrix = np.zeros((5, 5))
matrix += np.arange(5)
print(matrix)
# matrix with column values ranging form 0 to 4
matrix = matrix.T
print(matrix)

# 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)


def generate():
    for x in range(10):
        yield x
array = np.fromiter(generate(), dtype=int, count=-1)
print(array)

# 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)
vector = np.linspace(0, 1, 12, endpoint=True)[1: -1]
print(vector)

# 40. Create a random vector of size 10 and sort it (★★☆)
vector = np.random.random(10)
vector.sort()
print(vector)
print(np.random.random(10).sort())

# 41. How to sum a small array faster than np.sum? (★★☆)
array = np.arange(10)
np.add.reduce(array)

# 42. Consider two random array A and B, check if they are equal (★★☆)
A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
# Assuming identical shape of the arrays and a tolerance for the comparison of values
equal = np.allclose(A, B)
print(equal)

# 43. Make an array immutable (read-only) (★★☆)
array = np.zeros(10)
array.flags.writeable = False
# array[0] = 1

# 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)
matrix = np.random.random((10, 2))



