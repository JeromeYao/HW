#!/usr/bin/env python3
# Filename:NOP3C_C01_P05.py

'''
It's a note of 5th paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/yidao620c/python3-cookbook/blob/master/source/c01/p05_implement_a_priority_queue.rst
'''

__author__ = 'JeromeYao'

print('\n1.5 实现一个优先级队列\n')

'''
Q:怎样实现一个优先级排序的队列？ 
并且在这个队列上面每次pop操作总是返回优先级最高的那个元素
'''

# 利用 heapq 模块

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# 以上可以看出pop返回优先级最高的元素，若优先级一样则按照它们被插入到队列的顺序返回。

'''
 函数 heapq.heappush() 和 heapq.heappop() 分别在队列 _queue 上插入和删除第一个元素， 
 并且队列_queue保证第一个元素拥有最高优先级(1.4节已经讨论过这个问题)。 
 heappop() 函数总是返回"最小的"的元素，这就是保证队列pop操作返回正确元素的关键。 
 另外，由于push和pop操作时间复杂度为O(log N)，其中N是堆的大小，因此就算是N很大的时候它们运行速度也依旧很快。
'''
'''
a = Item('foo')
b = Item('bar')
a < b

Traceback (most recent call last):
Item('bar')
Item('spam')
  File "/home/jerome/GitEnvy4/PyNotes/NOP3C/NOP3C_C01_P05.py", line 65, in <module>
Item('foo')
    a < b
Item('grok')
TypeError: '<' not supported between instances of 'Item' and 'Item'

Process finished with exit code 1
'''

# 如果你使用元组 (priority, item) ，只要两个元素的优先级不同就能比较。
# 但是如果两个元素优先级一样的话，那么比较操作就会跟之前一样出错：

a = (1, Item('foo'))
b = (5, Item('bar'))
print(a < b)

'''
c = (1, Item('grok'))
a < c

Traceback (most recent call last):
  File "/home/jerome/GitEnvy4/PyNotes/NOP3C/NOP3C_C01_P05.py", line 88, in <module>
    a < c
TypeError: '<' not supported between instances of 'Item' and 'Item'

Process finished with exit code 1

'''

# 通过引入另外的 index 变量组成三元组 (priority, index, item) ，就能很好的避免上面的错误，
# 因为不可能有两个元素有相同的 index 值。
# Python在做元组比较时候，如果前面的比较已经可以确定结果了， 后面的比较操作就不会发生了：

a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
print(a < b)
print(a < c)

# 如果在多个线程中使用同一个队列，那么需要增加适当的锁和信号量机制。
