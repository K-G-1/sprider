# coding=UTF_8
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Firefox()
# driver.add_cookie({"Cookie": "ASP.NET_SessionId=ip1r4s55vwlg2x55kx1szy55"})
# driver.get("http://211.86.128.141/jwweb/MAINFRM.aspx")

with open('cookie.txt', 'r') as f:
    listCookies = f.read()
    print listCookies
for cookie in listCookies:
    driver.add_cookie(listCookies)
driver.get("http://211.86.128.141/jwweb/MAINFRM.aspx")    
while True:
    in_put = raw_input("do you want get cookies?")
    if in_put == 'Y':
        cookies = driver.get_cookies()
        file_name = open("cookie.txt", "a+")
        file_name.write(str(cookies)+'\n')
        print cookies
