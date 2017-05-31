import requests
from bs4 import BeautifulSoup
'''
r = requests.get('http://www.baidu.com', timeout=30)
r.encoding = r.apparent_encoding
'''

'''
def getHTMLtext(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'
if __name__ == '__main__':
    url ='http://www.baidu.com'
    print(getHTMLtext(url))
'''

'''
import requests
import time

starttime = time.clock()
url = "http://www.baidu.com"
for i in range(100):
    r = requests.get(url, timeout=10)
    if r.status_code != 200:
        print("ERROR. Can't get url for 100 times.")
        break
else:
    print("Get the url successfully.")
endtime = time.clock()
print("Total time is %.2fs" % (endtime - starttime))
'''

'''
r = requests.get('http://www.baidu.com')
print(r.status_code)
'''
'''
keyword = 'python'
try:
    kv = {'wd' : keyword}
    r = requests.get('http://www.baidu.com/s', params=kv)
    #r.encoding = r.apparent_encoding
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))

except:
    print('爬取失败')
'''

r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
#print(demo)
content =soup.body.contents
print(len(content))
print(content)
print(content[-2])

import re

# print(py*)
