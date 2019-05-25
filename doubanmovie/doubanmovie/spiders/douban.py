# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from doubanmovie.items import DoubanmovieItem

class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse_start_url(self, response):
        pass

    rules = (
        Rule(LinkExtractor(allow=r'start=.*?'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(restrict_xpaths='//span[@class="next"]/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = DoubanmovieItem()
        list = response.xpath('//div[@class="item"]')
        for listItem in list:
            item['title'] = listItem.xpath('.//div[@class="info"]//div[@class="hd"]/a/span[1]/text()').get()
            yield item
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
