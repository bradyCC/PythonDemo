# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import os


class TextPipeline(object):

    def __init__(self):
        pass
        self.file = codecs.open('text.json', 'w', 'utf-8')
        self.file.write('[')

    def open_spider(self, spider):
        print('This spider is starting!')

    def process_item(self, item, spider):
        if spider.name == 'ipProxy':
            data = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            self.file.write(data)
        return item

    def close_spider(self, spider):
        print('This spider is end!')
        self.file.seek(-2, os.SEEK_END)     # 定位到倒数第二个字符，即最后一个逗号
        self.file.truncate()                # 删除最后一个逗号
        self.file.write(']')
        self.file.close()
