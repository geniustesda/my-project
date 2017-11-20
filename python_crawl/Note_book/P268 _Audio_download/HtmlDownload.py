# -*- coding:utf8 -*-
"""网页下载到本地"""
import requests


class SpiderDownloader(object):
    def download(self, url):
        if url is None:
            return None
        user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
        headers = {'User-Agent': user_agent}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = "utf-8"
            return response.text
        return None
