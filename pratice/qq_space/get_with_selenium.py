# coding:utf-8
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# selenium中的actionchains的方法鼠标
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
def sele2req_cookie(cookies):
    cookie_dict = dict()
    for cookie in cookies:
        cookie_dict[cookie['name']] = cookie['value']
    return cookie_dict


login_url = 'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=手机QQ空间&pt_qr_link=https%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=https%3A//z.qzone.com/download.html&pt_no_auth=0'
# 创建的新实例驱动
options = webdriver.FirefoxOptions()
#火狐无头模式
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
driver = webdriver.Firefox(firefox_options=options)
driver.get(login_url)
driver.implicitly_wait(60)
#==================登录=======================#
time.sleep(3)
login_windows = driver.find_element_by_id('switcher_plogin')
login_windows.click()


username = driver.find_element_by_id('u')
username.clear()
password = driver.find_element_by_id('p')
password.clear()
username.send_keys('2060713822')
password.send_keys('662678guyi1105')

time.sleep(1)
submit = driver.find_element_by_id('login_button')
submit.click()
# time.sleep(5)

try:
    wait = WebDriverWait(driver, 3)
    input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'title-text ui-mr5')))
except:
    submit = driver.find_element_by_id('login_button')
    submit.click()
    print('click 2nd')   
    time.sleep(3)
    
print ('get url')
#============================================#
if __name__ == '__main__':
    while True:
        try:
            print ('start')           
            name = driver.find_element_by_xpath("//body/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/ul/li[1]/div[1]/div[4]/div[1]/a")
            print(name.text)
            time = driver.find_element_by_xpath('//body/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/ul/li[1]/div[1]/div[4]/div[2]/span')
            print (time.text)  
            zan = driver.find_element_by_xpath('//body/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/ul/li[1]/div[3]/div[1]/p/a[3]/i')
            zan.click()
            print ('ok') 
            driver.refresh()
        except:
            print("error")  

        # time.sleep(30)   
