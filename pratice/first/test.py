#coding=UTF_8
#first spider example
#

import urllib2
from sys import argv

script , url = argv

def download(url):
	print "Downloading:",url
	try:
		html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print 'download error',e.reason
		html = None
	return html


print  download(url)