#!usr/bin/env python
# Filename:guess_number.py

"""
猜数字游戏：
0～100内随机生成一个数，玩家猜测这个数是多少
可以控制猜测的次数。
"""

import random

x = random.randint(0, 100)
print(x)

times = int(input('输入你想猜的次数'))
num = int(input('输入你猜的数：'))

for i in range(0, times):
    if num < x:
        num = int(input('猜小了，请再输入：'))
    elif num > x:
        num = int(input('猜大了，请再输入：'))
    else:
        print('猜对了，厉害！')
        break
else:
    print('猜太多次了，BYE')


