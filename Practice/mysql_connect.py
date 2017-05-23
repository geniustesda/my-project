#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector


db = mysql.connector.connect(user='',password='',database='' )# mysql数据库的连接


cursor = db.cursor()


cursor.execute("SELECT VERSION()")


data = cursor.fetchone()

print "Database version : %s " % data


db.close()



