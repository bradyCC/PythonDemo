# -*- coding: utf-8 -*-
import scrapy
import json

class CatalogSpider(scrapy.Spider):
    name = 'catalog'
    allowed_domains = ['3.cn']
    start_urls = ['https://dc.3.cn/category/get']

    def parse(self, response):
        catalog_json = json.loads(
            str(response.body, encoding='gbk'),
            encoding='gbk'
        )
        result = []
        for data1 in catalog_json['data']:
            for data2 in data1['s']:
                url1 = data2['n'].split('|')[0]
                title1 = data2['n'].split('|')[1]
                result1 = {
                    'url': url1,
                    'title': title1,
                    'child': []
                }
                for data3 in data2['s']:
                    url2 = data3['n'].split('|')[0]
                    title2 = data3['n'].split('|')[1]
                    result2 = {
                        'url': url2,
                        'title': title2,
                        'child': []
                    }
                    for data4 in data3['s']:
                        url3 = data4['n'].split('|')[0]
                        title3 = data4['n'].split('|')[1]
                        result3 = {
                            'url': url3,
                            'title': title3
                        }
                    result2['child'].append(result3)
                result1['child'].append(result2)
            result.append(result1)
        print(result)
