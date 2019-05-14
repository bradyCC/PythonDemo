# -*- coding: utf-8 -*-
import scrapy
import logging
from copy import deepcopy

logger = logging.getLogger(__name__)

class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
       # 大分类数据
       list = response.xpath("//div[@class='menu-list']//div[@class='menu-item']")
       for a_list in list:
           item = {}
           item["a_class"] = a_list.xpath("./dl/dt/h3/a/text()").extract_first()
           item["a_href"] = a_list.xpath("./dl/dt/h3/a/@href").extract_first()
           sub_list = a_list.xpath("./dl/dd")
           for b_list in sub_list:
               item["b_class"] = b_list.xpath("./a/text()").extract()
               item["b_href"] = b_list.xpath("./a/@href").extract()
               yield scrapy.Request(
                   item["b_href"][0],
                   callback = self.parse_book_list,
                   meta = {"item": deepcopy(item)}
               )

    def parse_book_list(self, response):
        item = response.meta["item"]
        list = response.xpath("//div[@id='filter-results']//li")
        for l_list in list:
            item["book_name"] = l_list.xpath(".//p[@class='sell-point']/a/text()").extract_first()
        yield item