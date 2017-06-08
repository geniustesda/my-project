# -*- coding:utf-8 -*-
# !/usr/bin/env python
import requests
import re
from imp import reload

# 下面三行是编码转换的功能
import sys

reload(sys)

# hea是我们自己构造的一个字典，里面保存了user-agent。
# 让目标网站误以为本程序是浏览器，并非爬虫。
# 从网站的Requests Header中获取。【审查元素】
hea = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}

html = requests.get('http://jp.tingroom.com/yuedu/yd300p/', headers=hea)

html.encoding = 'utf8'  # 这一行是将编码转为utf-8否则中文会显示乱码。

# 此为正则表达式部分。找到规律，利用正则，内容就可以解析出来
title = re.findall('color:#666666;">(.*?)</span>', html.text, re.S)
# for each in title:
#     print(each+'\n')

chinese = re.findall('color: #039;">(.*?)</a>', html.text, re.S)
# for each in chinese:
#     print(each)

for i, j in zip(chinese, title):
    print(i + '\n' + j + '\n')