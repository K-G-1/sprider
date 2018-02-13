# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy import Request
from Ditf.items import DitfItem
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

class DarlingSpider(scrapy.Spider):
    name = 'darling'
    allowed_domains = ['www.acglala.com/']
    host = 'www.acglala.com/'
    start_urls = ['http://www.acglala.com/dhxf/DARLING0in0the0FRANKXX.html']
    xpath_str = "//*[@class='select-down']/div [@id='downswcont_01']/ul [@class='esp_con']/li[%s]/a"

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse_page)

    def parse_page(self,response):
        item = DitfItem()
        selector = Selector(response)
        for num  in range (1,12):
            #拼接字符串
            xpath = self.xpath_str %str(num)
            #打开路径
            content_list = selector.xpath(xpath)
            #找到特征 作为url
            urls = content_list.xpath('@href').extract_first()
            name = content_list.xpath('.//span/text()').extract_first()

            if urls is None:
                break
            else:
                urls = self.host + content_list.xpath('@href').extract_first()

            item['url'] = urls
            item['topic'] = name
            yield item
            # print urls 
            # print name
            
        
