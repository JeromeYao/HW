#!usr/bin/env python
# filename: jd_nutpro.py

"""
根据京东商城坚果pro手机销量
制作数据可视化分析
coding at jun. 2017
"""

import requests
import json


headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'club.jd.com',
    'Referer': 'https://item.jd.com/3867555.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
                  ' like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Cookie': 'B3C9B=Q',
}


def crawler(page):
    url = 'https://club.jd.com/comment/productPageComments.action?' \
          'callback=fetchJSON_comment98vv12621&' \
          'productId=4432058&' \
          'score=0&' \
          'sortType=5&' \
          'page={}&' \
          'pageSize=10&' \
          'isShadowSku=0&' \
          'fold=1'.format(page)
    result = requests.get(url, headers=headers, allow_redirects=True).text\
        .replace('fetchJSON_comment98vv12621(', '').replace(');', '')
    r = json.loads(result)
    for j in r['comments']:

        print('时间: {}'.format(j['creationTime']))
        print('颜色: {}'.format(j['productColor']))
        print('规格: {}'.format(j['productSize']))
        print('用户: {}'.format(j['userClientShow']))
        print('等级: {}'.format(j['userLevelName']))
        print('评分: {}'.format(j['score']))
        print('内容: {}'.format(j['content']))
        print('============================================')
    return result

if __name__ == '__main__':
    for i in range(2):
        res = crawler(i+1)
        print(res)
        print('第{}页 done'.format(i+1))
        with open('data_JD_demo.json', 'a+') as f:
            f.write(res)
            f.write('\n')
        # with open('data_JD_demo.txt', 'a+') as f1:
        #     f1.write()
