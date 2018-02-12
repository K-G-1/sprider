# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

class DarlingSpider(scrapy.Spider):
    name = "darling"
    allowed_domains = ["http://www.acglala.com"]
    host = 'http://www.acglala.com/'
    start_urls = (
        'http://www.acglala.com/dhxf/DARLING0in0the0FRANKXX.html',
    )

    def parse(self,response):
		# print response.body
		selector = Selector(response)
		# 在此，xpath会将所有class=topic的标签提取出来，当然这是个list
		# 这个list里的每一个元素都是我们要找的html标签
		content_list = selector.xpath("//*[@class='dh_outbox']")
		# 遍历这个list，处理每一个标签
		for content in content_list:
		# 此处解析标签，提取出我们需要的帖子标题。
			print content
			topic = content.xpath('string(.)').extract_first()
			print topic
			# # 此处提取出帖子的url地址。
			# url = self.host + content.xpath('@href').extract_first()
			# print url
