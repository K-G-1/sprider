#coding=UTF_8
#

import urllib2
from sys import argv 

script , url = argv

request = urllib2.Request(url)
try:
	urllib2.urlopen(request)
except urllib2.URLError,e:
	print e.reason
response = urllib2.urlopen(url)

print response.read()