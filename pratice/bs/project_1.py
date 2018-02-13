#!/usr/bin python3
#coding=UTF_8
#

import json
import requests, sys
from bs4 import BeautifulSoup


host = 'http://www.biqukan.com/'

# #class 下载小说
# class download(object):
#     """docstring for download"""
#     def __init__(self):
#         super(download, self).__init__()
#         self.url = 'http://www.biqukan.com/'
#         self.target = 'http://www.biqukan.com/17_17065/'
#         self.novels_name = ''
#         self.names = []
#         self.urls = []
#         self.nums = 0
#     #爬取目录 保存章节名与章节地址
#     def download_urls(self):
#         req = requests.get(url = self.target)
#         html = req.text
#         div_bf = BeautifulSoup(html,"lxml")
#         name = div_bf.find_all('h2')
#         self.novels_name = name[0].string
#         div = div_bf.find_all('div', class_ = 'listmain')
#         a_bf = BeautifulSoup(str(div[0]),"lxml")
#         a = a_bf.find_all('a')
#         self.nums = len(a[15:])                                #剔除不必要的章节，并统计章节数
#         for each in a[15:]:
#             self.names.append(each.string)
#             self.urls.append(self.url + each.get('href'))
#     #爬取章节内容
#     def get_contents(self, target):
#         req = requests.get(url = target)
#         html = req.text
#         bf = BeautifulSoup(html,"lxml")
#         texts = bf.find_all('div', class_ = 'showtxt')
#         texts = texts[0].text.replace('\xa0'*8,'\n\n')
#         return texts
#     #保存章节名，章节内容
#     def writer(self, name, path, text):
#         write_flag = True
#         with open(path, 'a', encoding='utf-8') as f:
#             f.write(name + '\n')
#             f.writelines(text)
#             f.write('\n\n')



# if __name__ == "__main__":
#     dl = download()
#     dl.download_urls()
#     print('《%s》开始下载：'%dl.novels_name)
#     save_name = dl.novels_name + '.txt'
#     print (save_name)
#     for i in range(dl.nums):
#         dl.writer(dl.names[i], save_name, dl.get_contents(dl.urls[i]))
#         sys.stdout.write("  已下载:%2.3f%%" %  float(i/dl.nums*100) + '\r')
#         sys.stdout.flush()
#     print('《%s》下载完成'%dl.novels_name)



if __name__ == '__main__':
    target = "http://www.biqukan.com/20_20951/8411339.html"
    req = requests.get(url = target)
    html = req.text
    bf = BeautifulSoup(html,'lxml')
    texts = bf.find_all('div',class_='showtxt')

    string = texts[0].text.replace('\xa0'*4,'\n\n')
    print (string)
    split_str = string[0:9]
    print (split_str)
#==============转化为字符串====================#
    # string = (str(texts[0])[34:].replace('<br/>','\n'))
    # split_str = string[0:4]
    # if split_str.isspace():
    #     print (' kon')
    # else :
    #     print('%s'%string[0:4])
#     target = 'http://www.biqukan.com/1_1094/'
#     req = requests.get(url = target)
#     html = req.text
#     div_bf = BeautifulSoup(html)
#     div = div_bf.find_all('div', class_ = 'listmain')
#     a_bf = BeautifulSoup(str(div[0]))
#     a = a_bf.find_all('a')
#     for each in a:
#         urls = host + each.get('href')
#         listmain = each.string
#         # print (listmain.rjust(40,' '),urls.rjust(100,' '))
#         print (listmain,urls)
#         # print ('{0:<10}{1:>70}'.format(each.string,))
#         # print ('{0:>10}'.format(host + each.get('href')))
