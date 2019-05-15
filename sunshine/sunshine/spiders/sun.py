# -*- coding: utf-8 -*-
import scrapy
import logging
from sunshine.items import SunshineItem

logger = logging.getLogger(__name__)

class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://sports.sun0769.com/ydzj']

    def parse(self, response):

        # 数据分组
        li_list = response.xpath("//div[@id='newslist-mainlist']//li")
        for li in li_list:
            item = SunshineItem()
            item["title"] = li.xpath("./h2/a/text()").extract_first()
            item["href"] = li.xpath("./h2/a/@href").extract_first()
            item["date_time"] = li.xpath("./dd/font/i/text()").extract_first()
            item["content"] = li.xpath("./dd/span/a/text()").extract_first()
            item["content_img"] = li.xpath("./dd/a/img/@src").extract_first()
            logger.warning(item)
        yield item
