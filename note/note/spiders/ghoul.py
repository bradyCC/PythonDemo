# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from note.items import NoteItem

class GhoulSpider(CrawlSpider):
    name = 'ghoul'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse_start_url(self, response):
        pass

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//article[@class="article-content"]//a'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = NoteItem()
        list = response.xpath('//div[@class="excerpts"]//article')
        for each in list:
            item['bookName'] = response.xpath('//h1[@class="focusbox-title"]/text()').get().split('：')[0]
            item['bookTitle'] = list.xpath('./a/text()').get().split(' ')[0]
            item['chapterNum'] = list.xpath('./a/text()').get().split(' ')[1]
            item['chapterTitle'] = list.xpath('./a/text()').get().split(' ')[2]
            item['chapterUrl'] = list.xpath('./a/@href').get()
            yield item
