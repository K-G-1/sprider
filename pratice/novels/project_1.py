#!/usr/bin python3
#coding=UTF_8
#

import json,time
import requests, sys
from bs4 import BeautifulSoup


host = 'http://www.biqukan.com/'

#class 下载小说
class download(object):
    """docstring for download"""
    def __init__(self):
        super(download, self).__init__()
        self.url = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/17_17957/'
        self.names = []
        self.urls = []
        self.nums = 0
    #爬取目录 保存章节名与章节地址
    def download_urls(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[12:])                                #剔除不必要的章节，并统计章节数
        for each in a[12:]:
            self.names.append(each.string)
            self.urls.append(self.url + each.get('href'))
    #爬取章节内容
    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_ = 'showtxt')
        #有的空4个字符有的空8个字符
        string = (str(texts[0])[34:].replace('<br/>','\n'))
        split_str = string[0:4]
        if split_str.isspace():
            texts = texts[0].text.replace('\xa0'*8,'\n\n    ')
            return texts
        else:
            return string
        
    #保存章节名，章节内容
    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

def check_in():
    if not sys.stdin.isatty():      # isatty() -> bool.  True if the file is connected to a TTY device.
        print ("Have data!")
        for line in sys.stdin:
            print (line)
        print ('end')
    else:
        print ('no data')


def check_input():
    import select
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        print ("Have data!")
        for line in sys.stdin:
            print ("%r"%line)
            if line  == 'q\n':
                return True
        return False
    else:
        return False

if __name__ == "__main__":
    dl = download()
    dl.download_urls()
    print('《一年永恒》开始下载：')
    for i in range(dl.nums):
        time.sleep(1)
        if  check_input():
            print ('break')
        else :
            pass
        # dl.writer(dl.names[i], '一念永恒.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" %  float(i/dl.nums*100) + '\r')
        sys.stdout.flush()


    # print('《一年永恒》下载完成')



# if __name__ == '__main__':
#     target = "http://www.biqukan.com/1_1094/5403177.html"
#     req = requests.get(url = target)
#     html = req.text
#     bf = BeautifulSoup(html)
#     texts = bf.find_all('div',class_='showtxt')
#     # print(texts[0].text.replace('\xa0'*8,'\n\n'))

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
