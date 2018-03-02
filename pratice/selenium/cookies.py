from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.baidu.com/")
print (driver.get_cookie('hello'))
d = {'hello':'python'}
for name,value in d.items():
    cookie = {
        'domain':   '.baidu.com',
        'name':     name,
        'value':    value,
        'expires':  '',
        'path':     '/',
        'httpOnly': False,
        'Hostonly': False,
        'secure':   False,
    }
    driver.add_cookie(cookie)
print(driver.get_cookie('hello'))