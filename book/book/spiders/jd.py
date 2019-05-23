# -*- coding: utf-8 -*-
import scrapy


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath("//div[@class='mc']/dl/dt")
        for dt in dt_list:
            item = {}
            item["b_cate"] = dt.xpath("./a/text()").extract_first()
            item["b_href"] = dt.xpath("./a/@href").extract_first()
            print(item)

