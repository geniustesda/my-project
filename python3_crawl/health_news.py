# -*- coding :utf-8 -*-

import requests
from bs4 import BeautifulSoup

# url = "http://health.sina.com.cn/healthcare/"
url = "http://health.sina.com.cn/"
response = requests.get(url)

response.encoding = ('utf-8')

soup = BeautifulSoup(response.text, 'html.parser')

for news in soup.select('.news-item', limit=10):
    if len(news.select('h2')) > 0:
        title = news.select('h2')[0].text
        time = news.select('.time')[0].text
        url = news.select('a')[0]['href']
        print(time + " " + title + " " + url)
        content = (time + ' ' + title + ' ' + url + '\n').encode('utf8')
        # print(type (content))

        f = open('./health.txt', 'a+')
        f.write(content)
        f.close()
    print("successfully!")
