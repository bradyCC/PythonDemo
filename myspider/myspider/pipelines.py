# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
# from pymongo import MongoClient

logger = logging.getLogger(__name__)
# client = MongoClient()
# collection = client['tencent']['hr']


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'itcast':
            # logger.warning('this is itcast-pipeline')
            pass
        return item


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'sun':
            # collection.insert(item)
            logger.warning('-'*20 + 'this is MyspiderPipelineSun' + '-'*20)
        return item
