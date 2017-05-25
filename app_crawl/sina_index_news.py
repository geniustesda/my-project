# -*- coding :utf-8 -*-

import requests
from bs4 import BeautifulSoup

res = requests.get('http://news.sina.com.cn/china/')


# res.encode = ('utf-8')
res.encode = ('')

soup = BeautifulSoup(res.text,'html.parser')

for news in soup.select('.news-item'):
    if len(news.select('h2')) > 0:
        h2 = news.select('h2')[0].text
        time = news.select('.time')[0].text
        a = news.select('a')[0]['href']
        print(time,h2.encode('gb18030'),a)


