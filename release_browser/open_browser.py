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

browser_stay_time = 5
chrome_driver = webdriver.Chrome(r'webdriver\chromedriver.80.exe')
chrome_driver.get('http://www.cueb.edu.cn')
time.sleep(browser_stay_time)
chrome_driver.close()


ie_driver = webdriver.Ie(r'webdriver\IEDriverServer.3.141.exe')
ie_driver.get('http://www.cueb.edu.cn')
time.sleep(browser_stay_time)
ie_driver.close()
