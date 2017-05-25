

```python
# -*- coding :utf-8 -*-

# http://health.sina.com.cn/healthcare/
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
        # table.write(id, 0, id + 1)
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

    5月25日 11:07,陈皮泡水喝的罕见功效,http://health.sina.com.cn/hc/2017-05-25/doc-ifyfqqyh8308163.shtml
    successfully!
    5月25日 06:30,不同虾吃法不同：这样的虾千万不能吃,http://health.sina.com.cn/hc/2017-05-25/doc-ifyfkkme0346417.shtml
    successfully!
    5月25日 06:30,这样吃梨润肺止咳,http://health.sina.com.cn/hc/2017-05-25/doc-ifyfqqyh8109081.shtml
    successfully!
    5月25日 06:30,必看！四种肉吃了会让你生病,http://health.sina.com.cn/hc/2017-05-25/doc-ifyfkqks4525395.shtml
    successfully!
    5月25日 06:30,6类食物加快代谢清肠道,http://health.sina.com.cn/hc/2017-05-25/doc-ifyfkqiv6747282.shtml
    successfully!
    5月25日 06:30,经常用眼吃点豌豆尖,http://health.sina.com.cn/hc/2017-05-25/doc-ifyfqqyh8108998.shtml
    successfully!
    5月25日 06:30,脾胃不好必喝4种祛湿汤,http://health.sina.com.cn/hc/2017-05-25/doc-ifyfkqwe0900789.shtml
    successfully!
    5月25日 06:30,四款汤让胸部更丰满,http://health.sina.com.cn/hc/2017-05-25/doc-ifyfkqwe0904036.shtml
    successfully!
    5月25日 06:30,常吃这几种食物有助燃烧脂肪,http://health.sina.com.cn/hc/2017-05-25/doc-ifyfkkme0339614.shtml
    successfully!
    5月25日 06:30,这些平民食物能代替高级营养品,http://health.sina.com.cn/hc/2017-05-25/doc-ifyfkkme0340035.shtml
    successfully!
    

 关于open()的mode参数：

 'r'：读

 'w'：写

 'a'：追加

 'r+' == r+w（可读可写，文件若不存在就报错(IOError)）

 'w+' == w+r（可读可写，文件若不存在就创建）

 'a+' ==a+r（可追加可写，文件若不存在就创建）

 对应的，如果是二进制文件，就都加一个b就好啦：

 'rb'　　'wb'　　'ab'　　'rb+'　　'wb+'　　'ab+'
