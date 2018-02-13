#!/usr/bin/env python
#coding=UTF_8

import urllib2
import re
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://www.opendv.com'



class display_opendv(object):
    def __init__(self,c_flag):
        super(display_opendv, self).__init__()
        self.continue_flag = c_flag
        self.response = ''
        self.content = ''
    def start(self):
        print "显示opendv.com"
        request = urllib2.Request(url)
        try:
            urllib2.urlopen(request)
        except urllib2.URLError,e:
            print e.reason
        self.response = urllib2.urlopen(url) 
        self.content = self.response.read().decode('utf-8')

    def disply(self):
        
        pattern = re.compile('<font size=.*?><b>(.*?)'+
                            '</b></font></p>.*?<p.*?>(.*?)</p>'+
                            '.*?<a href="(.*?)">.*?</a>',re.S)
        result1 = re.findall(pattern,self.content)

        for item in result1:
            print item[0],'\n',item[1],'\n',item[2]

a = display_opendv(False)
a.start()
a.disply()



