# !usr/bin/env python3
# Filename: weibo_spider.py

from selenium import webdriver
from splinter import Browser
import time

__author__ = 'JeromeYao'

mobile_emulation = {"deviceName": "Nexus 6P"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation",
                                       mobile_emulation)
browser = Browser('chrome', options=chrome_options)

url0 = 'https://passport.weibo.cn/signin/login'
browser.visit(url0)
browser.driver.set_window_size(400, 800)
time.sleep(2)

username_input = browser.find_by_xpath('//p[@class="input-box"]/input')[0]
username_input.type('jeromeyao_sh@163.com')
passwd_input = browser.find_by_xpath('//p[@class="input-box"]/input')[1]
passwd_input.type('wb199371')
btn_login = browser.find_by_id('loginAction')
btn_login.click()
time.sleep(1)

# js = "window.open('https://weibo.cn/search/');"
js = "window.open('https://weibo.cn/');"
browser.execute_script(js)
time.sleep(2)

browser.windows[0].close()
print("当前操作网页：" + browser.title)

"""
# 搜索微博关键字
text_serch = browser.find_by_name('keyword')
text_input = input('输入查找的关键字')
text_serch.fill(text_input)
btn_serch = browser.find_by_name('smblog')
btn_serch.click()
"""

# wb_text = input('请输入想要发布的微博')
wb_text = 'BB鸡正式启动嘿嘿嘿'

wb_textarea = browser.find_by_xpath("//textarea")
wb_textarea.fill(wb_text)
wb_submit = browser.find_by_xpath("//input[@value='发布']")[0]
wb_submit.click()
