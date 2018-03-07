from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://www.openedv.com/")
input("get_cookies?")
# 获取cookie并通过json模块将dict转化成str
dictCookies = driver.get_cookies()
jsonCookies = json.dumps(dictCookies)
# 登录完成后，将cookie保存到本地文件
with open('cookies.json', 'w') as f:
    f.write(jsonCookies)