# coding=UTF_8
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
           }

urls = 'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-17171595517.59.7b2364bcVeprbJ&id=559267040243&rn=44b0644b2e50d21a3f6d28246e8e15b1&abbucket=3'

response = requests.Session()
response = requests.get(url=urls, headers=headers)

div_bd = BeautifulSoup(response.text, "html.parser")
# print div_bd
price = div_bd.find_all('dl', class_='tb-metatit')
print price

