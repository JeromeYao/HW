# !usr/bin/env python3
# Filename: test.py

"""
这段测试代码可以模拟NEXUS 6P浏览器登录网页，
查看手机版网页源文件。
"""
from selenium import webdriver
from splinter import Browser


__author__ = 'JeromeYao'

mobile_emulation = {"deviceName": "Nexus 6P"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation",
                                       mobile_emulation)
browser = Browser('chrome', options=chrome_options)

url0 = 'https://m.baidu.com/'
browser.visit(url0)

