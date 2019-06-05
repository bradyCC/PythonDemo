# -*- coding: utf-8 -*-
import scrapy
from scrapyseleniumtest.items import ScrapyseleniumtestItem

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    # allowed_domains = ['www.taobao.com']
    # start_urls = ['http://www.taobao.com']
    start_urls = ['https://s.taobao.com/search?q=']

    def parse(self, response):
        print(response.url)

