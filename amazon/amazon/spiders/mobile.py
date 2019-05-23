# -*- coding: utf-8 -*-
import scrapy


class MobileSpider(scrapy.Spider):
    name = 'mobile'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dcomputers-intl-ship&field-keywords=%E6%89%8B%E6%9C%BA']

    def parse(self, response):
        titles = response.xpath("//div[@class='s-result-list sg-row']//div[contains(@class, 's-include-content-margin')]//a[contains(@class, 'a-link-normal')]/span/text()").extract()
        urls = response.xpath("//div[@class='s-result-list sg-row']//div[contains(@class, 's-include-content-margin')]//a[contains(@class, 'a-link-normal')]/@href").extract()
        imgs = response.xpath("//div[@class='s-result-list sg-row']//div[contains(@class, 's-include-content-margin')]//div[contains(@class, 'a-section aok-relative')]/img/@src").extract()