#!usr/bin python
# coding=UTF_8
import urllib2
from bs4 import BeautifulSoup
import re

# script , url = argv
url = 'http://www.weather.com.cn/weather/101220609.shtml'

request = urllib2.Request(url)
try:
    urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason
response = urllib2.urlopen(url)

# print response.read()

div_bd = BeautifulSoup(response, "html.parser")
index = div_bd.find_all('ul', class_='t clearfix')
# print (index[0].text)

sky = BeautifulSoup(str(index[0]), "lxml")

date = sky.find_all('h1')[0].string
weather = sky.find_all('p', class_='wea')
temperature = sky.find_all('p', class_='tem')
#=======================================#
pattern_wea = re.compile('.*?>(.*?)<.*?', re.S)

current_weather = re.findall(pattern_wea, str(weather[0]))
current_temp = re.findall('\d+', str(temperature[0]))
next_weather = re.findall(pattern_wea, str(weather[1]))
next_temp = re.findall('\d+', str(temperature[1]))


#========================================#
send_wea = "{'date':'3-1','weath':'%s','temperature':'%s-%s度',\
                    'next_weath':'%s','next_temperature':'%s-%s度'}" % (current_weather[0],current_temp[0],current_temp[1],next_weather[0],next_temp[0],next_temp[1])
print (send_wea)
