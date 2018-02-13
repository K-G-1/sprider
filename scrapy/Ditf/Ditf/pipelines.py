# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DitfPipeline(object):
    def __init__(self):
        #打开文件
        self.filename = open('example.txt', 'w')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.filename.write(line.decode("unicode-escape").decode('utf-8'))
        return item
