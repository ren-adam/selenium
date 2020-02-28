#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time: 2020-02-19 17:15
# @Project: selenium
# @Version: 2020.02 builder 191715
# @Author: Adam Ren
# @Email: adam_ren@sina.com
# @Github: https://github.com/ren-adam/selenium
# @Site: http://renpeter.com
# @File : open_browser.py
# @Software: PyCharm
#


import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


browser_stay_time = 5
# normal mode
chrome_driver = webdriver.Chrome(r'D:\extpath\selenium\webdriver\chromedriver.80.exe')
chrome_driver.get('http://www.cueb.edu.cn')
time.sleep(browser_stay_time)
chrome_driver.close()


ie_driver = webdriver.Ie(r'D:\extpath\selenium\webdriver\IEDriverServer.3.141.exe')
ie_driver.get('http://www.cueb.edu.cn')
time.sleep(browser_stay_time)
ie_driver.close()


# selenium no more support phantomjs
# phantomjs_driver = webdriver.PhantomJS(r'D:\extpath\selenium\webdriver\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# phantomjs_driver.get('http://www.cueb.edu.cn')
# time.sleep(browser_stay_time)
# print(phantomjs_driver.page_source)
# phantomjs_driver.close()


# headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_driver = webdriver.Chrome(executable_path=r'D:\extpath\selenium\webdriver\chromedriver.80.exe', options=chrome_options)
chrome_driver.get('http://www.cueb.edu.cn')
time.sleep(browser_stay_time)
print(chrome_driver.page_source)
chrome_driver.close()
