# coding=UTF_8
import requests

headers = {"Cookie": "ASP.NET_SessionId=40b5rrjhaoi4q5z5dzipj4nj",
           "Host": "211.86.128.141",
           "Referer": "http://211.86.128.141/jwweb/MAINFRM.aspx",
           "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
           }



r = requests.Session()
r = requests.get(url='http://211.86.128.141/jwweb/MAINFRM.aspx', headers=headers,
                 cookies={"Cookie": "ASP.NET_SessionId=iqosbu3uszzrfvqdtnn2h255"})
print (r.text)
headers['Referer'] = "http://211.86.128.141/jwweb/frame/menu.aspx"
r = requests.get('http://211.86.128.141/jwweb/xscj/Stu_MyScore.aspx',
                 headers=headers)
print (r.text)
headers['Referer'] = "http://211.86.128.141/jwweb/xscj/Stu_MyScore.aspx"
r = requests.get('http://211.86.128.141/jwweb/xscj/Stu_MyScore_rpt.aspx',
                  headers=headers)
r = requests.post('http://211.86.128.141/jwweb/xscj/Stu_MyScore_rpt.aspx',
                  headers=headers)
headers['Referer'] = 'http://211.86.128.141/jwweb/xscj/Stu_MyScore_rpt.aspx'
r = requests.get('http://211.86.128.141/jwweb/xscj/Stu_MyScore_Drawimg.aspx?x=1&h=2&w=915&xnxq=20170&xn=2017&xq=0&rpt=1&rad=2&zfx=0',
                 headers=headers)
print (r.text)
