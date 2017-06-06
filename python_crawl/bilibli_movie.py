#coding:utf-8
import _mysql,sys
import time
import socket
import random
import mysql.connector
from Queue import Queue
from threading import Thread
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities  #设置请求头

create_sql = """create table movie(id int(2) not null primary key auto_increment,
                              title varchar(200),
                              href text
                             )default charset=utf8;
             """

User_Agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/9.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"

    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50"
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)"
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)"
]


def store(title,url):
    cur.execute("insert into movie (title,href) VALUES (%s,%s)",(title,url))
    # cur.connection.commit()



def get_source(url):
    #service_args = ['--proxy=localhost:9150','--proxy-type=sock5'] #代理设置
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (random.choice(User_Agent_list))
    driver = webdriver.PhantomJS(executable_path=r'./phantomjs', desired_capabilities=dcap)   #,service_args=service_args ip代理设置

    try:
        driver.get(url)
    except Exception,e:
        print "此处出现异常,该异常信息为：%s" % e
        print "正在努力再尝试一次......"
        driver.get(url)
    time.sleep(5)
    html = driver.page_source
    driver.close()



    try:
        soup = BeautifulSoup(html, 'html.parser')
        a_list = soup.findAll("a", {"class": "preview"})
        a_page = soup.findAll("a", {"class":"p active"})[0]
        page = a_page.string
    except Exception,e:
        print "此处出现异常,该异常信息为：%s" % e

    print "\n"
    print "第 " + str(page) + " 页的电影集：\n\n"


    for a_each in a_list:
        movie_title = a_each.img['alt']
        movie_href = 'http://www.bilibili.com/' + a_each['href']
        print movie_title, movie_href
        print "正在向数据库导入电影信息："
        try:
            store(movie_title,movie_href)
        except _mysql.Error,e:
            print("数据库的Error %d:%s" % (e.args[0], e.args[1]))
            store(movie_title, movie_href)
        print "电影信息导入完毕"


if __name__ == "__main__":
    conn = mysql.connector.connect(host='127.0.0.1', user='root', passwd='123456', db='movie_info', port=3306,charset='utf8')
    cur = conn.cursor()  # cur 光标对象
    # cur.execute("use movie_info")
    # cur.execute("drop table movie")
    cur.execute(create_sql)

    q = Queue()
    for i in xrange(1,706):
        newpage = "http://www.bilibili.com/video/movie_west_1.html#!page=" + str(i)
        q.put(newpage)

    print "\n电影爬虫开始......\n"

    for i in xrange(1,706):
        t = Thread(target=get_source, args=(q.get(),))
        t.setDaemon(True)
        t.start()
        time.sleep(3)
        #socket.setdefaulttimeout(50)  # 设置10秒后连接超时
    t.join()

    print "\n数据抓取完毕\n"
    cur.close()
    conn.close()
    print "总部电影集导入数据库完毕"