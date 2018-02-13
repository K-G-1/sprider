# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


#引入文件
from scrapy.exceptions import DropItem
import json
import sys


reload(sys)
sys.setdefaultencoding('utf-8')


class MyPipeline(object):
    def __init__(self):
        #打开文件
        self.file = open('data.json', 'w')
        self.filename = open('example.txt', 'w')
    #该方法用于处理数据
    def process_item(self, item, spider):
        #读取item中的数据
        line = json.dumps(dict(item)) + "\n"
        #写入文件
        self.file.write(line.decode("unicode-escape").decode("utf-8"))
        self.filename.write(line.decode("unicode-escape").decode("utf-8"))
        #返回item
        return item
    #该方法在spider被开启时被调用。
    def open_spider(self, spider):
        pass
    #该方法在spider被关闭时被调用。
    def close_spider(self, spider):
        pass
