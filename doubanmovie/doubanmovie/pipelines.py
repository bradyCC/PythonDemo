# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DoubanmoviePipeline(object):

    def open_spider(self, spider):
        print('爬取开始')

    def process_item(self, item, spider):
        print(item)
        return item

    def close_spider(self, spider):
        print('爬取结束')