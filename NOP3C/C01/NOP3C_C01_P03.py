#!/usr/bin/env python3
# Filename:NOP3C_C01_P03.py

'''
It's a note of 3rd paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/yidao620c/python3-cookbook/blob/master/source/c01/p03_keep_last_n_items.rst
'''

__author__ = 'JeromeYao'

print('\n1.3 保留最后N个元素\n')

'''
Q:在迭代操作或者其他操作的时候，
怎样只保留最后有限几个元素的历史记录？
'''

# 保留有限记录可用collections.deque。
# 比如，下面的代码在多行上面做简单的文本匹配，
# 并返回匹配所在行的最后N行：

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

# Example use on a file
if __name__ == '__main__':
    with open('/home/jerome/Documents/test.txt') as f:
        for line, prevlines in search(f, '寒山', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

# 使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。
# 当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉。

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)
print('\n')

# deque 类可以被用在任何你只需要一个简单队列数据结构的场合。
# 如果你不设置最大队列大小，那么就会得到一个无限大小队列，
# 你可以在队列的两端执行添加和弹出元素的操作。

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.pop()
print(q)
q.popleft()
print(q)

# 在队列两端插入或删除元素时间复杂度都是 O(1) ，
# 而在列表的开头插入或删除元素的时间复杂度为 O(N) 。