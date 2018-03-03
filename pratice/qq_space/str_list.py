#!/usr/bin/python3
# coding:utf-8
import json
import requests

with open("selenium.json",'r') as r:
    ex_json_str = r.read()

new_dict = json.loads(ex_json_str)
# print(new_dict)
print(type(new_dict))
cookie_dict = dict()
for cookie in new_dict:
        cookie_dict[cookie['name']] = cookie['value']
print(cookie_dict)

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36'
    }

myspace = 'https://user.qzone.qq.com/2060713822'
content = requests.get(myspace, headers=headers, cookies=cookie_dict)
print(content.text)
with open("html1.txt",'w+')as f:
    f.write(content.text)