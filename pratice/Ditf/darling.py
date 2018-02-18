#!usr/bin python
# coding=UTF_8
#
import requests
import sys
from bs4 import BeautifulSoup
host = 'http://www.biqukan.com/'

target = 'https://pan.baidu.com/s/1jKioQOI#list/path=%2F2018n1%2Fdarling&parentPath=%2F2018n1'

req = requests.get(url=target)
html = req.text
print (html)
div_bd = BeautifulSoup(html, "lxml")
index = div_bd.find_all('a', class_='filename')
for Str in index:
    print (Str.string)
