#!/usr/bin/env python
#coding=UTF_8

import urllib2
import re
import sys


reload(sys)
sys.setdefaultencoding('unicode')

url = 'http://www.openedv.com/forum.php?mod=forumdisplay&fid=39'

# class file(object):
#     def __init__(self):
#         self.filename
#     def fileopen(self):
#         self.filename = open(corrlect.txt,'w')
#     def filewrite(self,str_innput):
#         write(str_innput)


class display_opendv(object):
    def __init__(self,c_flag):
        super(display_opendv, self).__init__()
        self.continue_flag = c_flag
        self.response = ''
        self.content = ''
    def start(self):
        F = open('corrlect.txt','w')
        print "显示opendv.com"
        request = urllib2.Request(url)
        try:
            urllib2.urlopen(request)
        except urllib2.URLError,e:
            print e.reason
        self.response = urllib2.urlopen(url) 
        self.content = self.response.read().decode('gbk')
        # print self.content
        # pattern = re.compile('<.*?class="s xst".*?>(.*?)</a>',re.S)
        pattern = re.compile('<.*?href="forum.php?mod=viewthread&tid=266356&extra=page%3D1".*?">',re.S)
        result1 = re.search(pattern,self.content)
        if result1:
            print result1
        # for item in result1:
        #     for string in item:
        #         print string,
        #     print  '\n'
        #     F.write(item)
        #     F.write('\n')
        # for item in result1:
        #     print item[0]


    def disply_list(self):
        pass

    def disply_detil(self):
        
        pattern = re.compile('<font size=.*?><b>(.*?)'+
                            '</b></font></p>.*?<p.*?>(.*?)</p>'+
                            '.*?<a href="(.*?)">.*?</a>',re.S)
        result1 = re.findall(pattern,self.content)

        for item in result1:
            print item[0],'\n',item[1],'\n',item[2]

a = display_opendv(False)
a.start()
a.disply_list()



