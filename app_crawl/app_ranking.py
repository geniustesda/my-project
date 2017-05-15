# -*-coding:utf8-*-
import requests
import re
import math

j = 1
#查看每一页都多少个APP，用于决定我们要翻多少页
html = requests.get('http://app.mi.com/topList')#获取网页的源代码
label = re.findall('<p class="app-desc">', html.text, re.S)#打开网页源码发现每个App名称前面有<p class="app-desc">，
# 所有统计这个标示的个数就可以知道每一页有多少个APP啦
pageAppNum = len(label)#label的长度就代表了每一页APP的个数

# print pageAppNum

print u'请输入App的数目：'
appNum = int(raw_input())
#根据要爬取的APP个数决定要翻多少页
pageNum = math.ceil(float(appNum) / pageAppNum)

for i in range(1, int(pageNum + 1)):
    html = requests.get('http://app.mi.com/topList?page=' + str(i))#括号内是每一页的连接地址
    # print html.text
    title = re.findall('</a><h5><a href=".*?">(.*?)</a></h5><p class="app-desc">', html.text, re.S)#找对应的APP的名称在网页中的位置，并用正则表达式来获取，如果看不懂，那你该好好去看看正则表达式了
    #将每一页的APP按先后顺序输出，知道第100个
    for each in title:
        if j <= appNum:
            print str(j) + ":" + each
        j = j + 1
        
        
        