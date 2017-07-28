# -*- coding:utf-8 -*-
"""
urllib练习，效果差强人意
"""
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import urllib2

content = urllib2.urlopen("http://weixin.sogou.com/").read().decode('utf-8')
# print(content)
# 目标区域
only_body = SoupStrainer("body")
soup = BeautifulSoup(content,"html.parser", parse_only=only_body)
for item in soup.find_all('a'):
    print(item.get('title'))
    print(item.get('href'))
