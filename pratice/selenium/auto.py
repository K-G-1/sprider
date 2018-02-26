from selenium import webdriver

import time

browser = webdriver.PhantomJS()
html = browser.get("http://www.opendv.com")
print html.text
# str_date = browser.find_element_by_class_name('')
# print str_date.text
# str_date = browser.find_elements_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr/td/p")
# for data in str_date:
#     print data.text
browser.close()