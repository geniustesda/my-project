# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import  re

# url = "http://health.sina.com.cn/healthcare/"
url = "http://health.sina.com.cn/"
response = requests.get(url)

response.encoding = ('utf-8')

soup = BeautifulSoup(response.text, 'html.parser')

for news in soup.select('.news-item', limit=5):
    if len(news.select('h2')) > 0:
        title = news.select('h2')[0].text
        time = news.select('.time')[0].text
        url = news.select('a')[0]['href']
        abstract = (time + ' ' + title + ' ' + url).encode('utf8')
    print(abstract)

    # 写入txt文件
    # f = open('./health.txt', 'a+')
    # f.write(abstract)
    # f.close()

    response_content = requests.get(url)
    response_content.encoding = ('utf8')

    content = BeautifulSoup(response_content.text,'html.parser')

    reg = re.compile(r'<p>.*?</p>')
    for text in content.select('.content'):
        if len(text.select('p'))>0:
            # text = text.select('p')[0].text
            reg.findall(str(text))
    # print(type(text))
    print(str(text)+'\n')


