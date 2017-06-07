# -*-coding:utf8-*-
import requests
import re
import math


html = requests.get('http://app.mi.com/topList')#获取网页的源代码
label = re.findall('<p class="app-desc">', html.text, re.S)#打开网页源码发现每个App名称后面都有<p class="app-desc">，
# 所以统计这个标签的个数就可以知道每一页有多少个APP啦
pageAppNum = len(label)#通过len()方法来计算label的个数，从而获取当前页面App的个数
# print pageAppNum #计算一页的最大app数量

print u'请输入期望获取的App数目：'
appNum = int(raw_input()) #手动输入app数量
pageNum = math.ceil(float(appNum)/pageAppNum) #将输入的期望值除以每一页最大值获得总页数,ceil是为了获取整数页数


print "打印到第%d"%pageNum+"页："

j = 1 #初始化一个变量
for i in range(1, int(pageNum + 1)):
    html = requests.get('http://app.mi.com/topList?page=' + str(i))#通过递增i的值来获取下一页的app
    # print html #打印页面
    title = re.findall('</a><h5><a href=".*?">(.*?)</a></h5><p class="app-desc">', html.text, re.S)#找对应的APP的名称在网页中的位置，并用正则表达式来获取
    #将每一页的APP按先后顺序输出

    #打印输出的格式
    for each in title:
        if j <= appNum:
            print str(j) + ":" + each
        j += 1


