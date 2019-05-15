# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CircPipeline(object):

    def open_spider(self, spider):
        print('The spider is starting!')
        self.fp = open('./data.txt', 'w')

    def process_item(self, item, spider):
        self.fp.write(item['title'] + ':' + item['public_date'] + '\n')
        return item

    def close_spider(self, spider):
        print('End!')
        self.fp.close()