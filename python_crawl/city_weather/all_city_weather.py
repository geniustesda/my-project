# -*- coding:utf8 -*-
'''
通过调用高德地图的API获取文件列表内的城市天气,需要设置成自己的key,并且在高德后台添加IP白名单
'''
import requests
import pymongo
import json
import re

KEY = "0411c73f7d7766aeb2dbb38935112575&extensions=all"

def get_city():
    lines = []
    with open("./cityfile.txt", 'r',encoding="utf-8") as f:
        lines.append(f.readlines())
        lines = lines[0]
        print(lines)
        return lines

def find_weather(city):
    # 通过API获取json数据
    url = "http://restapi.amap.com/v3/weather/weatherInfo?city="\
          + city + "&key="+KEY
    print(url)
    response = requests.get(url).text
    return response


def save_data(response):
    # 将数据转换成dict格式
    data = json.loads(response)["forecasts"][0]
    # 连接mongodb,数据库名称为test,数据表名为weather_info
    client = pymongo.MongoClient('localhost', 27017)
    db = client["weather"]
    collection = db["weather_info"]
    # 第二种写法
    # db = client.test
    # collection = db.userinfo

    # 修改_id值,并保存数据,save保存比insert慢
    data['_id'] = data["adcode"]
    collection.insert(data)
    return data

if __name__ == '__main__':
    citys = get_city()
    for city in citys:
        pattern = re.compile(r"\n")
        content = re.split(pattern, city)[0]
        print (content)
        response = find_weather(content)
        print(response)
        try:
            info = save_data(response)
        # 出现没有的城市继续运行
        except:
            continue
        print (info)

