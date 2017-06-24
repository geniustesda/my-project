# -*-coding:utf8-*-
import requests
import re
import math

# 获取网页的源代码
html = requests.get('http://app.mi.com/topList')

# 打开网页源码发现每个App名称后面都有<p class="app-desc">,所以统计这个标签的个数就可以计算出每一页有多少app了
label = re.findall('<p class="app-desc">', html.text, re.S)

# 通过len()方法来计算label的个数，从而获取当前页面App的个数
pageAppNum = len(label)
print ("每一页app个数为%d，共%d页"%pageAppNum)

print u'请输入期望获取的App数目：'

# 手动输入app数量
appNum = int(raw_input())
# 将输入的期望值除以每一页最大值获得总页数,ceil是为了获取整数页数
pageNum = math.ceil(float(appNum)/pageAppNum)


print ("打印到第%d"%pageNum+"页：")

# 初始化一个变量
j = 1
for i in range(1, int(pageNum + 1)):
    # 通过递增i的值来获取下一页的app
    html = requests.get('http://app.mi.com/topList?page=' + str(i))
    # 打印页面
    print (html)

    # 找对应的APP的名称在网页中的位置，并用正则表达式来获取
    title = re.findall('</a><h5><a href=".*?">(.*?)</a></h5><p class="app-desc">', html.text, re.S)

    # 打印结果
    for each in title:
        if j <= appNum:
            print str(j) + ":" + each
        j += 1


