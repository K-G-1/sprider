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
# from time import sleep
# from pyvirtualdisplay import Display

# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# display = Display(visible=0, size=(800, 800))
# display.start()

log_file = open('zan.txt','w+')
log_file.write('test')

def login_in(login_url,driver):
    driver.get(login_url)
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
    time.sleep(1)
    print(driver.current_url)

def get_space():
    try:
        wait = WebDriverWait(driver, 5)
        input = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'title-text ui-mr5')))
    except:
        print('click 2nd')
        try:
            submit = driver.find_element_by_id('login_button')
            submit.click()
        except:
            print('2nd click error')    
    print(driver.current_url)

login_url = 'https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=手机QQ空间&pt_qr_link=https%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=https%3A//z.qzone.com/download.html&pt_no_auth=0'
# 创建的新实例驱动
options = webdriver.FirefoxOptions()
# 火狐无头模式
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
driver = webdriver.Firefox(firefox_options=options)
driver.get(login_url)
driver.implicitly_wait(30)
#==================登录=======================#
# time.sleep(3)
# login_windows = driver.find_element_by_id('switcher_plogin')
# login_windows.click()


# username = driver.find_element_by_id('u')
# username.clear()
# password = driver.find_element_by_id('p')
# password.clear()
# username.send_keys('2060713822')
# password.send_keys('662678guyi1105')

# time.sleep(1)
# submit = driver.find_element_by_id('login_button')
# submit.click()
# time.sleep(1)

# try:
#     wait = WebDriverWait(driver, 5)
#     input = wait.until(EC.presence_of_element_located(
#         (By.CLASS_NAME, 'title-text ui-mr5')))
# except:
#     print('click 2nd')
#     try:
#         submit = driver.find_element_by_id('login_button')
#         submit.click()
#     except:
#         print('2nd click error')
    # time.sleep(3)
# page_get = input("login in ?(Y/N)")
# while page_get is 'N':
#     submit = driver.find_element_by_id('login_button')
#     submit.click()
#     page_get = input("login in ?")



#============================================#
if __name__ == '__main__':
    login_in(login_url,driver)
    get_space()
    # import time
    # faild_times = 0
    # old_name = '1'
    # current_name = '0'
    # old_time = '0'
    # current_time = '0'
    # while True:
    #     # time.sleep(3)
        
    #     # print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    #     try:
    #         driver.refresh()
    #         time.sleep(2)
    #         # print ('start')

    #         # time.sleep(60)
    #         try:
    #             wait = WebDriverWait(driver, 5)
    #             name = wait.until(EC.presence_of_element_located(
    #                 (By.XPATH, "//body/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/ul/li[1]/div[1]/div[4]/div[1]/a")))
    #             name = driver.find_element_by_xpath(
    #                 "//body/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/ul/li[1]/div[1]/div[4]/div[1]/a")
    #             # print(name.text)
    #             current_name = name.text
    #             contiue = True
    #         except:
    #             # print('not name')
    #             contiue = False

    #         if contiue is True:
    #             try:
    #                 pub_time = driver.find_element_by_xpath(
    #                     '//body/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/ul/li[1]/div[1]/div[4]/div[2]/span')
    #                 # print (pub_time.text)
    #                 current_time = pub_time.text

    #                 if (old_name != current_name) and (old_time != current_time):
    #                     zan = driver.find_element_by_xpath(
    #                         '//body/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div/ul/li[1]/div[3]/div[1]/p/a[3]/i')
    #                     zan.click()
    #                     print(current_time)
    #                     print(current_name)
    #                     print('click ok ')
    #                     print(faild_times)
    #                     faild_times = 0
    #                     print ('\r\r')
    #                     old_name = current_name
    #                     old_time = old_time
    #             except:
    #                 faild_times = faild_times +1
    #                 # print("not time")
    #         # time.sleep(1)
    #     except:
    #         faild_times = faild_times +1
    #         # print("error")
    #         # driver.refresh()

    driver.close()
