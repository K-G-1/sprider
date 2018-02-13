# -*- coding: utf-8 -*-
import scrapy
from moocproject.items import CourseItem

class MoocSpider(scrapy.Spider):
    name = "mooc"
    #设定域名
    allowed_domains = ["imooc.com"]
    #填写爬取地址
    start_urls = ["http://www.imooc.com/course/list"]
    #编写爬取方法
    def parse(self, response):
        #实例一个容器保存爬取的信息
        item = CourseItem()
        #这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        #先获取每个课程的div
        for box in response.xpath('//div[@class="course-card-container"]/a[@class="course-card"]'):
            #获取每个div中的课程路径
            item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
            #获取div中的课程标题  
            item['title'] = box.xpath('.//h3/text()').extract_first()  
            # item['title'] = item['title'].decode('UTF-8')
            # 获取div中的学生人数
            item['student'] = box.xpath('.//span[2]/text()').extract_first()
            #获取div中的课程简介
            item['introduction'] = box.xpath('.//p/text()').extract_first()
            #返回信息
            yield item
           
