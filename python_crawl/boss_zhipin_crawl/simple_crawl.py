# -*- coding:utf-8 -*-
"""
python3下运行，python2会有编码问题
功能：用来爬取和显示网页的demo
"""
import requests
import webbrowser
from lxml import etree
import time

headers = {
        # 'Host': 'www.zhipin.com',
        'Upgrade-Insecure-Requests': '1',
        # 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
    }


def get_cookie():
    url = "http://www.zhipin.com"
    response = requests.get(url, headers=headers, timeout=10)
    print(response.cookies)
    return response.cookies


def requests_view(response):
    requests_url = response.url
    print(requests_url)
    base_url = "<head><base href='%s'>" % (requests_url)
    content = response.content.replace(b"<head>", base_url)
    tem_html = open("tmp.html", "wb")
    tem_html.write(content)
    tem_html.close()
    webbrowser.open_new_tab("tmp.html")


def html_parse(response):
    html = etree.HTML(response.content)
    city = html.xpath(".//*[@id='main']/div[3]/div[2]/ul/li/div[1]/div[1]/p/text()[1]")
    working_life = html.xpath(".//*[@id='main']/div[3]/div[2]/ul/li/div[1]/div[1]/p/text()[2]")
    education = html.xpath(".//*[@id='main']/div[3]/div[2]/ul/li/div[1]/div[1]/p/text()[3]")
    company_name = html.xpath(".//*[@id='main']/div[3]/div[2]/ul/li/div[1]/div[2]/div/h3/a/text()")
    positions = html.xpath(".//*[@id='main']/div[3]/div[2]/ul/li/div[1]/div[1]/h3/a/text()")
    money = html.xpath(".//*[@id='main']/div[3]/div[2]/ul/li/div[1]/div[1]/h3/a/span/text()")
    industry = html.xpath(".//*[@id='main']/div[3]/div[2]/ul/li/div[1]/div[2]/div/p/text()[1]")
    financing = html.xpath(".//*[@id='main']/div[3]/div[2]/ul/li/div[1]/div[2]/div/p/text()[2]")
    company_size = html.xpath(".//*[@id='main']/div[3]/div[2]/ul/li/div[1]/div[2]/div/p/text()[3]")
    company_info_detail_url = html.xpath(".//*[@id='main']/div[3]/div[2]/ul/li/div[1]/div/h3/a/@href")
    for a, b, c, d, e, f, g, h, i in zip(city, working_life, education, company_name, positions, money, industry, financing, company_size):
        print (a + " " + b + " " + c + " " + d + " " + e + " " + f + " " + g + " " + h + " " + i + "\n\n")
    return company_info_detail_url


def city_list(city):
    city_code = {
        "全国": "c100010000",
        "上海": "c101020100",
        "北京": "c101010100",
        "深圳": "c101280600",
        "杭州": "c101210100",
    }
    if city_code[city]:
        return city_code[city]


def get_max_page_num():
    pass


def url_lists(city_code, position):
    number = 1
    url_list = []
    url_list.append("https://www.zhipin.com/" + city_code + "/h_101020100/?query=" + position + "&page=" + str(number) + "&ka=page-" + str(number))
    return url_list

if __name__ == '__main__':
    city = "上海"
    city_code = city_list(city)
    print(city_code)
    position_lists = ['python', 'java', '前端', '机器学习', '测试']
    for p in position_lists:
        url_list = url_lists(city_code, p)
        cookies = get_cookie()

        for url in url_list:
            response = requests.get(url, headers=headers, cookies=cookies, timeout=10)
            # requests_view(response)  # 默认浏览器显示网页
            html_parse(response)
            time.sleep(3)