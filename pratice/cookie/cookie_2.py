# coding=UTF_8
import requests
from lxml import html
headers = {
    "Host": "211.86.128.141",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
}
cookie = {'Cookies' = "UM_distinctid=1613b9ec4fe7b1-02b12f3c0773bf-7c2d6751-100200-1613b9ec4ff41e; CNZZDATA1257047916=1641486711-1517121715-null%7C1518496792; bdshare_firstime=1517123716448; Hm_lvt_c49232a8be82d37340e295f04cb9cf85=1518274068,1518281309,1518365690,1518442497; nqdR_2132_pc_size_c=0; nqdR_2132_sid=B1CYgw; nqdR_2132_saltkey=jh9XvFcf; nqdR_2132_lastvisit=1519698609; nqdR_2132_lastact=1519709883%09plugin.php%09; nqdR_2132_ulastactivity=1959G6WJ%2BrL3FE108TYRKUHGio4Se153rTMSRLuI9J3OcZo0cFv%2B; nqdR_2132_auth=35e6wUvXsuJQM%2F%2B%2Fq5EuTy%2BZTb0nVAxMY6XR2acltwNxmC0tSccK1Z2rTJDYE3mrd0fCvWGJSFAnc9bSdy6gZoGDLA; nqdR_2132_lastcheckfeed=57932%7C1519702261; acw_tc=AQAAAAK5xi19EgoADllFeXrH6B4OLGvc; nqdR_2132_lip=121.69.89.14%2C1519702261; nqdR_2132_nofavfid=1"}




r = requests.Session()
r = requests.get(url='http://www.openedv.com/', headers=headers)

html = html.fromstring(r.text) 
li = html.xpath("//body/div[4]/div/div[2]/ul/li[2]/a/text()")
print (li[0])
head = html.xpath("//div[@class='avt y']")
for url in head:
    urls = url.xpath('.//@herf')
    print(urls)
