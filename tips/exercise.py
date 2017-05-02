#!/usr/bin/env python3
# Filename:exercise.py

''


print('n = 123')
print('f = 456.789')
print("s1 = 'Hello, world'")
print("s2 = 'Hello, \\Adam\\''")
print('''s3 = r\'Hello, "Bart"\'''')
print("r'''Hello,\nLisa!'''")
obj = b"ABC"
print(obj)
print(type(obj))
print("\n")

'''
问：小明的成绩从去年的72分提升到了今年的85分，
请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
'''

s1 = 72
s2 = 85
r = (s2-s1) / s2 *100.0
#print(type(r))
print("%.1f%%" %r)
print("\n")


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
print("\n")

'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）
帮小明计算他的BMI指数，并根据BMI指数：
低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''

height =1.75
weight = 80.5
bmi = weight / (height**2)
if bmi < 18.5 :
    print ("过轻")
elif bmi < 25 :
    print("正常")
elif bmi < 28 :
    print("过重")
elif bmi < 32 :
    print("肥胖")
else :
    print("严重肥胖")
print("\n")


'''
d ={(1,[2,3]): 10}
print(d[(1,[2,3])])
'''
n1 = 255
n2 = 1000
n1_16 = hex(n1)
n2_16 = hex(n2)

print(n1_16,n2_16)
#print("%s\n%s"%(n1_16,n2_16))



'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax^2 + bx + c = 0

的两个解。

提示：计算平方根可以调用math.sqrt()函数：
'''
import math

def quadratic(a, b, c) :
    #a , b ,c =input("请输入a,b,c三个参数")
    delta = b**2 - 4*a*c

    #if not isinstance((a,b,c),(int,float)) :
    #    raise TypeError('bad operand type')
    if a == 0:
        return "该方程不为一元二次方程"
    elif delta< 0 :
        return "该方程无解"
    else :
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1,x2
print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)
print('\n')

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=[], *d, kw):
    c.append('The End')
    print('a =', a, 'b =', b, 'c =', c,'d =', d, 'kw =', kw)
    print('\" %s %s %s %s \"'%(a,b,c,kw))
f1(1,2)
f2(1, 2, kw=9)
f2(1, 2, kw=11)
print('\n')

L1 = ['Hello','World',18,'Apple',None]
#L2 = [s.lower() for s in L1 if isinstance(s,str)]
L2=[s.lower() if isinstance(s,str) else  s for s in L1]
print(L2)
print(type(L2[2]))
print('\n')

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(10))
for n in fib(10):
    print(n)
print('\n')

#杨辉三角

def triangles():
    L = [1]
    while True :
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
print('\n')

seq = '0123456789'
print(seq[0])
print(seq[-1])
print(seq[1:5])
print(seq[7:])
print(seq[-3:])
print(seq[:3])
print(seq[:])
print(seq[::2])
print(seq[::-2])
print(seq[9:1:-1])
print([0,1,2]+[1,2,3])
print([0,1,2]*3)
print([None]*10)
print(1 in [1,2,3])
print("% 10s" % "----")
print({'title' : 'TITLE','body':'BODY'})
print(dict(title = "title", body = "body"))
print(dict([("title", "title"), ("body", "body")]))
dic = {"title": "title", "body": "body"}
print(dic["title"])
del dic["title"]
print(dic)
print(' ' == " ")
print([ ] == ' ')
print(0 < 1 < 10)
print(0 < 1 < 10)
print('\n'*3)
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x == y)
print(x == z)
print(x is y)
print(x is z)

for key in {"x":"xxx"}.values():
    print(key)

for index, value in enumerate(range(0, 10)):
    print(index, value)

from functools import reduce
def fn(x, y):
        return x * 10 + y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print(reduce(fn, map(char2num, '13579')))
print('\n')


def normalize(name):
    return name.lower().capitalize()

print(normalize('sadAEWfs'))


#测试
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce
def prod(L):
    return reduce(lambda x,y : x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def str2float(s):
    return

print('str2float(\'123.456\') =', str2float('123.456'))
print('\n')

def is_palindrome(n):
    return str(n) == str(n)[::-1]
output = filter(is_palindrome, range(1, 1000))
print(list(output))
print('\n')

# by_name 通过名字来排列
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]


def by_name(t):
    return t

L2 = sorted(L,key=by_name)
print(L2)

# by_score 通过分数来排列
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_score(t):
    return t[:][1]

L2 = sorted(L, key=by_score, reverse=True)
print(L2)
print('\n')


def by_name(t):
    return t


def by_score(t):
    return t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)
L3 = sorted(L, key=by_score, reverse=True)
print(L3)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L2 = sorted(L, key=lambda x : x[0]) #根据名字排列
print(L2)
L3 = sorted(L, key=lambda x : x[1], reverse=True) #根据成绩排列
print(L3)
print('\n')


def lazy_sum(*args):
    def sum1():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum1
f = lazy_sum(1, 3, 5, 7, 9)

print(lazy_sum(1,3,5,7,9))
print(lazy_sum(1,3,5,7,9)())
print(f)
print(f())
print('\n')


def count():
    def f(j):
        return lambda : j*j
#等价于：
#        def g():
#            return j*j
#        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print(type(f1))
print('%d %d %d' % (f1(), f2(), f3()))
print("\n")


def now():
    print('2017.3.7')
f = now
f()
print(now.__name__)
print(f.__name__)
print('\n')


def log(func):
    def wrapper(*args, **kw):
        print('call %s():'%func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print("2017.3.7")
now()
print('\n')


def int2(x, base=2):
    return int(x, base)
print(int2("100000", 17))
print('\n')


class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

print('\n')

class Student(object):
    pass

s = Student()
s.name = "Michael"
print(s.name)


def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

s2 = Student()
#s2.set_age(25)


def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)

class Student(object):
    __slots__ = ['name', 'age']
    __slots__.append('score')

s =Student()
s.name = 'Micheal007'
s.age = 26

s.score =98
print('\n')

print(s.name)
print(s.age)
print(s.score)


try:
    print('try...')
    r =10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


print('\n')

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('End')
'''
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')

'''

class LowerLetters(object):
    def __init__(self):
        self.current = 'a'

    def __next__(self):
        if self.current > 'z':
            raise StopIteration
        result = self.current
        self.current = chr(ord(result)+1)
        return result

    def __iter__(self):
        return self

letters = LowerLetters()
for i in letters:
    print(i)
print(dir(LowerLetters()))
print(type(LowerLetters()))
print('\n')


def countdown(n):
    print('Counting down from', n)
    while n > 0:
        yield n
        n -= 1
x = countdown(10)
print(x)
print('\n')

def is_palindrome(n):
    return str(n) == str(n)[::-1]
output = filter(is_palindrome, range(1, 1000))
print(list(output))
