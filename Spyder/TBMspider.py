#!usr/bin/env python3
# Filename: TBMspider.py


from selenium import webdriver
from splinter import Browser


__author__ = 'JeromeYao'

mobile_emulation = {"deviceName": "Nexus 6P"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation",
                                       mobile_emulation)
browser = Browser('chrome', options=chrome_options)

url0 = 'https://m.taobao.com/'
# goods = "书包"
# url0 = 'https://s.m.taobao.com/h5?q=' + goods
browser.visit(url0)
browser.driver.set_window_size(400, 800)

# xpath(//div[@class="main"]/div[@class="price"])  # 商品页面内价格标签
