# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

# 访问链接
driver = webdriver.Firefox()
url = "http://lib.csdn.net/"
driver.get(url)
elem_div = driver.find_elements_by_xpath("//ul[@class='list01 clearfix']/li/div[2]/a")

# 获取当前窗口句柄
now_handle = driver.current_window_handle
print now_handle

for elem in elem_div:
    print elem.text  # 获取正文
    print elem.get_attribute('href')  # 获取属性值

# 点击进入新的界面 _blank弹出
elem.click()

# 获取所有窗口句柄
all_handles = driver.current_window_handle

# 弹出两个界面,跳转到不是主窗体界面
for handle in all_handles:
    if handle != now_handle:
        # 输出待选择的窗口句柄
        print handle
        driver.switch_to_window(handle)
        time.sleep(1)

        print u'弹出界面信息'
        print driver.current_url
        print driver.title

        # 获取登录连接信息
        elem_p = driver.find_element_by_xpath(
            "//div[@class='coltop clearfix']/div[2]")
        print elem_p.text

        # 关闭当前窗口
        driver.close()

# 输出主窗口句柄
print now_handle
driver.switch_to_window(now_handle)  # 返回主窗口 开始下一个跳转
