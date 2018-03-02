from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Firefox()
driver.get("http://www.opendv.com/")
# print driver.page_source
#=========================================#
class_name = driver.find_element_by_class_name("STYLE3")
xpath_name = driver.find_element_by_xpath("//tbody/tr/td/p[2]/font/b")
buttun  = driver.find_element_by_xpath("//tbody/tr/td/p[4]/a")

print class_name.text
print xpath_name.text
print buttun.text

buttun.click()

#=======================================#

driver.close()
