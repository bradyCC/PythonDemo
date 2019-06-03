# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from text.items import TextItem

class IpproxySpider(CrawlSpider):
    name = 'ipProxy'
    # allowed_domains = ['superfastip.com']
    start_urls = ['http://www.superfastip.com/welcome']

    def parse_start_url(self, response):
        print(response.url)

    rules = (
        Rule(LinkExtractor(allow=r'http://www.superfastip.com/welcome/freeip/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
        item = TextItem()
        list = response.xpath('//div[@class="row clearfix"][2]//table/tbody/tr')
        for listItem in list:
            type = str(listItem.xpath('.//td[4]/text()').get()).lower()
            ip = str(listItem.xpath('.//td[1]/text()').get())
            port = str(listItem.xpath('.//td[2]/text()').get())
            item['ipAddress'] = type + '://' + ip + ':' + port
            item['ipCheck'] = ip + ' ' + port
            yield item
