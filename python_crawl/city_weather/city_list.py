# -*- coding: utf-8 -*-
'''
简单的爬取城市列表，有一些地名没有更新
'''

import requests
from lxml import etree

r = requests.get("http://www.52maps.com/china_city.php#0")
html = etree.HTML(r.content)
content = html.xpath('.//*[@class="col-md-12"]/a/text()')

for i in content:
    i = i.encode("utf-8")
    if i != None:
        f = open("./cityfile.txt", 'a+')
        f.write(i + "\n")
    else:
        break