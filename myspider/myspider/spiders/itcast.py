# -*- coding: utf-8 -*-
import scrapy
import logging
logger = logging.getLogger(__name__)


# 创建scrapy项目 scrapy startproject 项目名
# 创建爬虫 scrapy genspider 爬虫名 爬取地址
# 启动爬虫 scrapy crawl itcast
class ItcastSpider(scrapy.Spider):
    name = 'itcast'                                                     # 爬虫名
    allowed_domains = ['itcast.cn']                                     # 允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']         # 最开始请求的url地址

    def parse(self, response):
        # 处理 start_urls 地址对应的响应
        # ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret1)

        # 分组
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = {}
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            logger.warning(item)
            yield item
