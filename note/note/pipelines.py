# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo

class NotePipeline(object):

    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBMAME']
        client = pymongo.MongoClient(host=host, port=port)


    def open_spider(self, spider):
        print('Starting!')

    def process_item(self, item, spider):
        print(item)
        return item

    def close_spider(self, spider):
        print('End!')
