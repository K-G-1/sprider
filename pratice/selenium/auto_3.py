# coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# selenium中的actionchains的方法鼠标
from selenium.webdriver.common.action_chains import ActionChains
import time


# # 创建的新实例驱动
# options = webdriver.FirefoxOptions()
# #火狐无头模式
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Firefox(firefox_options=options)
driver.get("https://www.gn00.com/")

#==================登录=======================#
login_windows = driver.find_element_by_xpath(
    "//body/div[4]/div/div[3]/div/a[3]")
login_windows.click()

time.sleep(1)
# print (driver.page_source)
login_name = driver.find_element_by_xpath(
    '//div[@class="c cl"]/div[1]/table/tbody/tr/td/input[@name = "username"]')
#python3 发送中文的时候要加上‘u'
#python2 没有解决
login_name.send_keys(u"顾影_")
login_password = driver.find_element_by_xpath(
    '//div[@class="c cl"]/div[2]/table/tbody/tr/td/input[@name = "password"]')
login_password.send_keys("662678guyi1105GUYI")
time.sleep(1)
button = driver.find_element_by_xpath(
    "//div[@class='rfmrig rfmrig_login']/button[@name='loginsubmit']")
# print(buttun.text)
button.click()


#==================签到=====================#
#延时4秒返回登录前页面
#也可以尝试点击’返回页面‘
time.sleep(4)
#鼠标悬停，不然隐藏元素出不来
mouse = driver.find_element_by_id('qing_user')
ActionChains(driver).move_to_element(mouse).perform()

##鼠标时间不是很准确，最好加上延时
sign_in = driver.find_element_by_xpath('//div[@id="qing_user_menu"]/a[2]/font')
print(sign_in.text)
sign_in.click()
time.sleep(1)

string_text = driver.find_element_by_xpath('//li[@id="kx"]')
string_text.click()

sign_button = driver.find_element_by_xpath('//button[@class="pn pnc"]')
print(sign_button.text)
sign_button.click()

#=======================================#
time.sleep(5)
driver.close()
