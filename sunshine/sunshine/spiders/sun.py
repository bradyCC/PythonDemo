# -*- coding: utf-8 -*-
import scrapy
import logging
from sunshine.sunshine.items import SunshineItem

logger = logging.getLogger(__name__)

class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://news.sun0769.com/national']

    def parse(self, response):

        # 数据分组
        li_list = response.xpath("//div[@id='newslist-mainlist']//li")
        for li in li_list:
            item = SunshineItem()
            item["title"] = li.xpath("./h2/a/text()").extract_first()
            item["content"] = li.xpath("./dd/span/a/text()").extract_first()
            item["href"] = li.xpath("./h2/a/@href").extract_first()
            item["date_time"] = li.xpath("./dd/font/i/text()").extract_first()
            logger.warning(item)
        yield item

        # 下一页
        # next_url = response.xpath("//div[@id='newslist-pages']//li[@class='page-next']/a/@href").extract_first()
        # if next_url != 'http://i.sun0769.com/was5/web/search?channelid=50439&ChnlName=%E5%9B%BD%E5%86%85%E6%96%B0%E9%97%BB&searchword=docchannel=8235':
        #     next_url = 'http://news.sun0769.com/national/' + next_url
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.parse
        #     )
