#!/usr/bin/env python3
# Filename:NOP3C_C01_P02.py

'''
It's a note of 2nd paragraph of 1st chapter of python3-cookbook chinese version
https://github.com/yidao620c/python3-cookbook/blob/master/source/c01/p02_unpack_elements_from_iterables.rst
'''

__author__ = 'JeromeYao'


print('\n1.2 解压可迭代对象赋值给多个变量\n')

'''
Q:如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。
 那么怎样才能从这个可迭代对象中解压出N个元素出来？
'''

# 星号表达式可以一战


def drop_first_last(grades):
    first, *middles, last = grades
    return avg(middles)


def avg(middles):
    return sum(middles)/len(middles)

f = drop_first_last([2, 3, 4, 5, 6])
print(f, '\n')


# 另外一种情况，假设你现在有一些用户的记录列表，每条记录包含一个名字、邮件，接着就是不确定数量的电话号码。
# 你可以像下面这样分解这些记录：
record = ('Dave', 'dave@example.com', '772-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print('name:%s\nemail:%s\nphone_numbers:%s' % (name, email, phone_numbers))
print('type of phone_numbers:', type(phone_numbers))
# 星号表达式解压出的变量永远都是列表类型(包括元素数量为0时，此时输出为[]）


def avg_comparison(sales_record):
    *trailing_qtrs, current_qtr = sales_record
    trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
    return '%.2f %d' % (trailing_avg, current_qtr)
sales_record_now = [10, 8, 7, 1, 9, 5, 10, 3]
print(avg_comparison(sales_record_now))
print('\n')

# 星号表达式在迭代元素为可变长元组的序列时是很有用的。
# 比如，下面是一个带有标签的元组序列：
records = [
    ('foo', 1, 2, 3, 4),
    ('bar', 'hello'),
    ('foo', 5, 6),
]


def do_foo(*x):
    print('foo', x)


def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
print('\n')

# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割。
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

print('uname:%s\nhomedir:%s\nsh:%s\n' % (uname, homedir, sh))

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print('name:%s\nyear:%s' % (name, year))
print('\n')

# 递归算法星号解压的运用
items = [1, 10, 7, 4, 5, 9]


def sum1(items):
    head, *tail = items
    return head + sum1(tail) if tail else head
print(sum1(items))