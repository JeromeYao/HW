#!/usr/bin/env python3
# Filename:NOP3C_C01_P04.py

'''
It's a note of 4th paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/yidao620c/python3-cookbook/blob/master/source/c01/p04_find_largest_or_smallest_n_items.rst
'''

__author__ = 'JeromeYao'

print('\n1.4 查找最大或最小的N个元素\n')

'''
Q:怎样从一个集合中获得最大或者最小的N个元素列表？
'''

#heapq模块有两个函数：nlargest() 和 nsmallest() 可以完美解决这个问题。

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # prints [42, 37, 23]
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]
print('\n')

# 这两个函数都能接收关键字，用于更复杂的数据结构中。
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print('three of the cheapest:%s\nthree of the most expensive:%s' % (cheap, expensive))
print('\n')

# 如果你想在一个集合中查找最小或最大的N个元素，并且N小于集合元素数量，那么这些函数提供了很好的性能。
# 因为在底层实现里面，首先会先将集合数据进行堆排序后放入一个列表中：
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(nums)
print(nums)

# 堆数据结构最终要的特征是heap[0]永远为最小元素。
# 剩余N-1个元素可用heapq.heappop()方法弹出
# 该方法会先将第一个元素弹出来，然后用下一个最小的元素来取代被弹出元素(这种操作时间复杂度仅仅是O(log N)
heapq.heappop(nums)
print(nums)
heapq.heappop(nums)
print(nums)
heapq.heappop(nums)
print(nums)

'''
当要查找的元素个数相对比较小的时候，函数 nlargest() 和 nsmallest() 是很合适的。 
如果你仅仅想查找唯一的最小或最大(N=1)的元素的话，那么使用 min() 和 max() 函数会更快些。 
类似的，如果N的大小和集合大小接近的时候，通常先排序这个集合然后再使用切片操作会更快点
( sorted(items)[:N] 或者是 sorted(items)[-N:] )。 
需要在正确场合使用函数 nlargest() 和 nsmallest() 才能发挥它们的优势 
(如果N快接近集合大小了，那么使用排序操作会更好些)。
'''