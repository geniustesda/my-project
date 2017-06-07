# -*- coding:utf-8 -*-
import scrapy
from ..items import ZufangItem

class GanjiSpider(scrapy.Spider):
    name = "zufang"
    # allowed_domains = ["http://sh.ganji.com/fang1/"]
    start_urls = ['http://sh.ganji.com/fang1//']

    def parse(self, response):
        print(response)
        zf = ZufangItem()
        title_lists = response.xpath('.//*[@class="f-list-item "]/dl/dd[1]/a/text()').extract()
        money_lists = response.xpath('.//*[@class="f-list-item "]/dl/dd[5]/div[1]/span[1]/text()').extract()
        
        for i,j in zip(title_lists,money_lists):
            zf['title'] = i
            zf['money'] = j
            yield zf
            yield(i,":",j)


            
