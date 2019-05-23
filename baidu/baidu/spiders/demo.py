# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=XPath&rsv_spt=1&rsv_iqid=0xe2cbb44c001d6e7f&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100&rsv_t=7e98ncsj2fijkYq%2BT8LTl%2BuMMUFo0m9lwRGdz7psxyrj3e8%2FLHr1QQiG5PAfyeuVEJyK&rsv_sug2=0&inputT=2301&rsv_sug4=2301']

    def parse(self, response):
        print(response.xpath("//div[@class='opr-recommends-merge-content']//div[contains(@class, 'opr-recommends-merge-item')]//div[@class='c-gap-top-small']/a/text()").extract())
        pass
