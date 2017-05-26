#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
获取新浪网页新闻，并写入txt文档和数据库
"""
import requests
from bs4 import BeautifulSoup
import re

# 目标网站地址
# url = "http://news.sina.com.cn/"
url = "http://health.sina.com.cn/"
response = requests.get(url)
response.encoding = ('utf8')

soup = BeautifulSoup(response.text, 'html.parser')
for news in soup.select('.news-item', limit=5):
    if len(news.select('h2')) > 0:
        title = news.select('h2')[0].text
        time = news.select('.time')[0].text
        url = news.select('a')[0]['href']
        abstract = (time+' '+title+' '+url).encode('utf8')
    print(abstract)

    # 将标题等信息写入txt文件
    f = open('./health.txt', 'a+')
    f.write(abstract)
    f.close()

    # 打开链接列表，获取正文网页
    response_content = requests.get(url)
    response_content.encoding = ('utf8')

    # 通过正则和BeautifulSoup提取文章内容信息
    content = BeautifulSoup(response_content.text,'html.parser')
    reg_p = re.compile(r'<p>.*?</p>')
    reg_sub_p = re.compile('<[^>]+>')
    for text in content.select('.content'):
        if len(text.select('p')) > 0:
            # text = text.select('p')[0].text
            reg_p.findall(str(text))
            result = reg_sub_p.sub("", str(text))
    print(str(result) + '\n')

    # 将文章内容写入txt文件

    # 将文章内容写入数据库文件

