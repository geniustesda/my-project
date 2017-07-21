# -*- coding:utf8 -*-
'''
通过调用高德地图的API手动查询目的城市天气
'''
import requests
import pymongo
import json

def find_weather(city):
    # 通过API获取json数据
    url = "http://restapi.amap.com/v3/weather/weatherInfo?city="\
          + city + "&key=0411c73f7d7766aeb2dbb38935112575&extensions=all"
    response = requests.get(url=url).text
    # 将数据转换成dict格式
    return response

def save_data(response):
    # 连接mongodb,数据库名称为test
    data = json.loads(response)
    client = pymongo.MongoClient('localhost', 27017)
    db = client["test"]
    collection = db["userinfo"]
    # 第二种写法
    # db = client.test
    # collection = db.userinfo

    # 保存数据
    collection.save(data)

if __name__ == '__main__':
    city = raw_input("请输入查询城市的天气名称：")
    response = find_weather(city)
    save_data(response)
    print (response)