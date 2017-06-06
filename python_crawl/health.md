```python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import codecs

# url = "http://health.sina.com.cn/healthcare/"
url = "http://health.sina.com.cn/"
response = requests.get(url)

response.encoding=('utf-8')

soup = BeautifulSoup(response.text,'html.parser')

for news in soup.select('.news-item',limit=10):
    if len(news.select('h2')) > 0:
        title = news.select('h2')[0].text
        time = news.select('.time')[0].text
        url = news.select('a')[0]['href']
        print(time+","+title+","+url)
        content = time+','+title+','+url+'\n'
        #print(type (content))
        
        #将数据写入txt文件
        f = open('./health.txt', 'a+')
        f.writelines(content)
        f.close()
    print("successfully!")
        
```
    

 关于open()的mode参数：

 'r'：读

 'w'：写

 'a'：追加

 'r+' == r+w（可读可写，文件若不存在就报错(IOError)）

 'w+' == w+r（可读可写，文件若不存在就创建）

 'a+' ==a+r（可追加可写，文件若不存在就创建）

 对应的，如果是二进制文件，就都加一个b就好啦：

 'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+'
