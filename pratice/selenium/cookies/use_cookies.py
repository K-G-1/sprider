from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.implicitly_wait(10)
# 初次建立连接，随后方可修改cookie
browser.get("http://www.openedv.com/")
# 删除第一次建立连接时的cookie
browser.delete_all_cookies()
# 读取登录时存储到本地的cookie
with open('cookies.json', 'r', encoding='utf-8') as f:
    listCookies = json.loads(f.read())
for cookie in listCookies:
    browser.add_cookie({
        'domain': '.openedv.com',  # 此处xxx.com前，需要带点
        'name': cookie['name'],
        'value': cookie['value'],
        'path': '/',
        'expires': None
    })
# 再次访问页面，便可实现免登陆访问
try:
    browser.get("http://www.openedv.com/")

    sign_in_button = browser.find_element_by_id('dcsignin_tips')
    sign_in_button.click()

    sign_text = browser.find_element_by_id('emot_1')
    sign_text.click()
except:
    print("未登录成功/以签到")
try:
    check_button = browser.find_element_by_xpath('//p[@class="o pns"]/button[@class="pn pnc"]')
    check_button.click()
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print("ok\r")
except:
    print("error")
#必须要有延时不然不能签到成功
time.sleep(5)
browser.close()