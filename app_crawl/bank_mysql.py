#!/usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1',port='3306',user='root',password='xinya.com123',database='testdb',charset='utf8')
cur = conn.cursor()

#创建数据表
cur.execute("create table if not EXISTS account(accid int(10) PRIMARY KEY,money int(10)")

#插入两行数据
cur.execute('insert into account(accid ,money)VALUES(1,110)')
cur.execute('insert into account(accid ,money)VALUES(2,10)')

cur.close()
conn.close()