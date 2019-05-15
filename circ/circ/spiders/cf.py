# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['circ.gov.cn']
    start_urls = ['http://circ.gov.cn/']

    # 定义提取url地址规则
    rules = (
        # LinkExtractor 链接提取器：提取url地址
        # callback 提取出来的url地址的response会交给callback处理
        # follow 当前url地址的响应是否重新经过rules来提取url地址
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    # parse函数有特殊功能，不能定义
    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
