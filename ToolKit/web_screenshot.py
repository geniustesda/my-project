# -*- coding:utf8 -*-
# ! /user/bin/python

from selenium import webdriver
import time

# 目标网站爬取列表
urllist = [
	'http://www.baidu.com',
	'http://www.qq.com/',
	'https://www.taobao.com/',
	'http://weibo.com/',
	]

# 选择爬取的用浏览器
driver = webdriver.PhantomJS("./phantomjs.exe")
i = 0
for url in urllist:
	driver.get(url)
	time.sleep(3)
	driver.get_screenshot_as_file('./picture/'+str(i)+'_screenshot.png')
	i += 1

