# -*- coding:utf-8 -*-
# ! user/bin/python
""" python2.7
获取目标网址的图片并且保存到本地，相对路径和绝对路径都可以
"""
import requests
from lxml import etree
from urlparse import urljoin
import os
import re

# 图片存储路径
IMG_DIR = "pic"
if os.path.exists(IMG_DIR) == False:
    os.mkdir(IMG_DIR)

# 图片地址获取，并且保存图片数据到本地
def get_img_information(web_url,web_title,web_img_url):
    # 输入图片的基本信息
    url_base = raw_input("请输入图片网址的url：")
    title_xpath = raw_input("请输入标题的xpath：")
    img_url_xpath = raw_input("请输入图片的xpath：")

    # 如果未输入内容，则使用默认内容
    if url_base == "":
        url_base = web_url
    else:
        pass
    if title_xpath == "":
        title_xpath = web_title
    else:
        pass
    if img_url_xpath == "":
        img_url_xpath = web_img_url
    else:
        pass

    response = requests.get(url_base)
    response.encodig = ('utf-8')
    response = response.content
    selector = etree.HTML(response)
    title = selector.xpath(title_xpath)
    img_url = selector.xpath(img_url_xpath)

    count = 1
    for i, j in zip(title, img_url):
        img_data_url = urljoin(url_base, j)
        i = "".join(i.split())
        src = (str(count)+i + " " + img_data_url).encode('utf-8')
        print(src)

        # 将图片信息保存到文本文件
        f = open('./pic/img_information.txt', 'a+')
        f.write(src + '\n')
        f.close()
        
        # 将二进制图片内容保存到指定文件夹
        with open('./pic/{}'.format(count)+'.jpg.png', 'wb+') as file:
            try:
                img_data = requests.get(img_data_url).content
                file.write(img_data)
                count += 1
            except:
                print("picture save error!")
        file.close()

if __name__ == "__main__":

    # 默认图片地址信息
    img_base_url = "http://588ku.com/beijing/0-0-dnum-0-8-0-0-0-1/"
    title_xpath = ".//*[@id='index-flex-images']/div/div[3]/text()"
    img_xpath = ".//*[@id='index-flex-images']/div/div[1]/a/img/@data-original"

    get_img_information(img_base_url, title_xpath, img_xpath)

