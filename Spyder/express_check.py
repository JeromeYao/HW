#!usr/bin/env python3
# Filename:  express_check.py

"""
该程序用来检查快递当前进度。
模拟手机百度网页版查询快递100
"""
from selenium import webdriver
from splinter import Browser
import time

__author__ = 'JeromeYao'

mobile_emulation = {"deviceName": "Nexus 6P"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation",
                                       mobile_emulation)
with Browser('chrome', options=chrome_options, headless=True) as browser:
    url0 = 'https://m.baidu.com/s?word=kuaidi100'
    browser.visit(url0)
    time.sleep(1)
    username_login = browser.find_by_id('J-wa-express-delivery-num')
    # username_input = input('需要查询的快递号：')
    username_input = 'EK821562900GB'
    username_login.fill(username_input)
    browser.find_by_xpath("//div[@class='c-gap-top']/button").click()
    time.sleep(1)
    info_output = browser.find_by_xpath("//div[@class='c-color wa-express-delivery-info']").text
    time_output = browser.find_by_xpath("//p[@class='c-color-gray wa-express-delivery-time c-gap-top-small']")\
        .first.text
    localtime = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time()))
    print('最后位置：{}\n消息时间：{}\n查询时间：{}\n'.format(info_output, time_output, localtime))
    with open('/home/jerome/Documents/script/express_info.txt', 'a+') as f:
        f.write('\n最后消息：{}\n消息时间：{}\n查询时间：{}\n-------------------------------------\n'
                .format(info_output, time_output, localtime))
