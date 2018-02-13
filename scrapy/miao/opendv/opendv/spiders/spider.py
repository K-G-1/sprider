# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy import Request


class SpiderSpider(scrapy.Spider):
    name = "spider"
    host = 'http://www.openedv.com/'
    host1= 'http://www.openedv.com/forum-2-1.html'
    allowed_domains = ["http://www.openedv.com"]
    start_urls = (
        'http://www.openedv.com/forum-2-1.html',
    )

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse_page)

    def parse_topic(self, response):
        print "start"

    def parse_page(self,response):
        selector = Selector(response)
        content_list = selector.xpath("//*[@class='s xst']")
        for content in content_list:
            # topic = content.xpath('string(.)').extract_first()
            # print topic
            #此处提取出帖子的url地址。
            urls = self.host + content.xpath('@href').extract_first()
            yield Request(url=self.host1, callback=self.parse_topic)
            print urls
            

    
    # def parse_topic(self,response):
    #     print 'start'
    #     selector = Selector(response)
    #     content_list = selector.xpath("//*[@tr]")
    #     print content_list
    #     print 'finish'
    #     # for content in content_list:
    #     #     topic = content.xpath('string(.)').extract_first()
    #     #     print topic


    # def parse(self, response):
    #     print response.body
	#   def parse(self,response):
		# # print response.body
		# selector = Selector(response)
		# # 在此，xpath会将所有class=topic的标签提取出来，当然这是个list
		# # 这个list里的每一个元素都是我们要找的html标签
		# content_list = selector.xpath("//*[@class='s xst']")
		# # 遍历这个list，处理每一个标签
		# for content in content_list:
		# # 此处解析标签，提取出我们需要的帖子标题。
		# 	# print content
		# 	topic = content.xpath('string(.)').extract_first()
		# 	print topic
		# 	# 此处提取出帖子的url地址。
		# 	url = self.host + content.xpath('@href').extract_first()
		# 	print url
		# 	

