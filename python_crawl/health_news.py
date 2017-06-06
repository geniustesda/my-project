#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
获取新浪网页新闻，并写入txt文档和数据库
"""
import requests
from bs4 import BeautifulSoup
import re
import mysql.connector

# 目标网站地址
# url = "http://news.sina.com.cn/"
url = "http://health.sina.com.cn/"
response = requests.get(url)
response.encoding = ('utf8')
count = 100
soup = BeautifulSoup(response.text, 'html.parser')
for news in soup.select('.news-item',limit=100):
    if len(news.select('h2')) > 0:
        title = news.select('h2')[0].text
        time = news.select('.time')[0].text
        url = news.select('a')[0]['href']
        abstract = (time+' '+title+' '+url+'\n').encode('utf8')

    # 单独将标题等信息写入txt文件
    f = open('./health_title.txt', 'a+')
    f.write(abstract+'\n')
    f.close()

    # 打开正文链接，获取文章的网页
    response_content = requests.get(url)
    response_content.encoding = ('utf8')

    # 通过正则和BeautifulSoup提取文章内容信息
    content = BeautifulSoup(response_content.text,'html.parser')
    reg_p = re.compile(r'<p>.*?</p>')
    reg_sub_p = re.compile(r'<[^>]+>')
    reg_img = re.compile(r'<img.*?src="(http://.*?)".*?>')

    for texts in content.select('.content'):
        if len(texts.select('p')) > 0:
            tag_p = reg_p.findall(str(texts))
            result = reg_sub_p.sub("", str(texts))
            img_url = re.findall(reg_img,str(texts))
        print(time+' '+title+' '+url)
        print(str(img_url) +'\n')

    # 将文章标题和内容写入txt文件
    f = open('./health_content.txt', 'a+')
    f.write(abstract+result+'\n')
    f.close()

    # 将文章内的照片存储到本地
    news_summary = (count,time,title,url,'None')
    with open('./pic/{}'.format(count)+'_'+title+'.jpg.png', 'wb+') as file:
        try:
            img_data = requests.get(img_url[0]).content
            file.write(img_data)
            count += 1
        except:
            pass

    # 将文章的标题和内容写入数据库
    db = mysql.connector.connect(host='localhost',user='root',passwd='passwd',db='test')
    cur = db.cursor()

    create_database = """CREATE DATABASE IF NOT EXISTS test;"""
    create_table = """
                    CREATE TABLE IF NOT EXISTS news(id int(10),news_time VARCHAR(10),news_title VARCHAR(40),
                    news_url VARCHAR(200),news_contents VARCHAR(4096));"""
    insert_content = """
                    INSERT INTO news(id,news_time,news_title,news_url,news_contents)
                    VALUES(%d,'%s','%s','%s','%s');""" % news_summary
    delete_content = """
                    DELETE FROM news WHERE 1;
                    """

    cur.execute(create_database)
    cur.execute(create_table)
    cur.execute(insert_content)
    # cur.execute(delete_content)
    db.commit()
    db.close()

