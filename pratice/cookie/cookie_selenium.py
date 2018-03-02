from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("http://www.openedv.com/")
print driver.page_source

in_put = raw_input("save cookie?")
cookie = driver.get_cookies()
if in_put is 'Y':
    with open('sele_cookie.txt','w+') as f:
        f.write(str(cookie))
        f.write('\r\n')