#!usr/bin/env python3
# Filename:  pyspider_model.py

import requests

"""
requests库
"""
__author__ = 'JeromeYao'


def get_html_text(url, headers):
    try:
        r = requests.get(url, headers, allow_redirects=True)
        e = r.raise_for_status()
        # r.encoding = r.apparent_encoding
        return r.text
    except e:
        return '抓取异常'


if __name__ == "__main__":
    url0 = "http://jandan.net"
    headers0 = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        # 'Host': '',
        # 'Referer': '',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
                      ' like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        # 'Cookie': '',
    }
    print(get_html_text(url0, headers=headers0))
