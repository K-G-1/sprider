#!usr/bin python
# coding=UTF_8
import requests
import sys
from bs4 import BeautifulSoup
import time

host = 'http://www.weather.com.cn/weather/101220609.shtml'

req = requests.get(url=host)
html = req.text
print (html)
# div_bd = BeautifulSoup(html, "html.parser")
# index = div_bd.find_all('ul',class_='t clearfix')
# print (index[0].text)
# sky = BeautifulSoup(str(index[0]), "lxml")
# weather = sky.find_all('p',class_= 'wea')
# print (weather[0].string)
