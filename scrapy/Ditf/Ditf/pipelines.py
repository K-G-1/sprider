# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class DitfPipeline(object):
    def __init__(self):
        # 打开文件
        self.filename = open('example.txt', 'w',encoding = 'utf-8')

    def process_item(self, item, spider):
        # line = json.dumps(dict(item)) + "\n"
        str_symptom = str(item)+ '\n'
        # print('%r'%str_symptom)
        self.filename.write(str_symptom)
        return item
