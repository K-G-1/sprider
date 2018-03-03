# coding:utf-8
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# selenium中的actionchains的方法鼠标
from selenium.webdriver.common.action_chains import ActionChains
import time
# from pyvirtualdisplay import Display

# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# display = Display(visible=0, size=(800, 800))
# display.start()

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36'
    }
myspace = 'https://user.qzone.qq.com/2060713822'


with open("selenium.json",'r') as r:
    ex_json_str = r.read()

new_list = json.loads(ex_json_str)
# print(new_list[1])
# print(type(new_list))
# cookie_dict = dict()
for cookie in new_list:
    print(cookie['domain'])          

# print (cookie_dict)
# 创建的新实例驱动
options = webdriver.FirefoxOptions()
#火狐无头模式
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
driver = webdriver.Firefox(firefox_options=options)
driver.get(myspace)
for cookie in new_list:
    driver.add_cookie({
        'domain': 'i.qq.com',  # 此处xxx.com前，需要带点
        'name': cookie['name'],
        'value': cookie['value'],
        'path': cookie['path'],
        'expires': None
    })

# time.sleep(5)
# driver.close()