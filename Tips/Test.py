#!usr/bin/env python3
# Filename:Test.py

"""
For test
"""

import requests

url = 'https://item.jd.com/4869176.html'
kv = {'user-agent': 'Mozilla/5.0'}

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
    with open('zcn.txt', 'a') as f:
        f.write(r.text)
except :
    print('出现异常')



