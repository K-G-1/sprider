#!usr/bin python
# coding=UTF_8
#
import requests
import sys
from bs4 import BeautifulSoup
host = 'http://www.biqukan.com/'


# class 下载小说
class download(object):
    """docstring for download"""

    def __init__(self):
        super(download, self).__init__()
        self.url = 'http://www.biqukan.com'
        self.target = 'http://www.biqukan.com/paihangbang/'
        self.novels_name = ''
        self.names = []
        self.urls = []
        self.index = 0
        self.index_urls = []
        self.nums = 0

    # 爬取排行榜
    def get_url_list(self):
        req = requests.get(url=self.target)
        html = req.text
        div_bd = BeautifulSoup(html, "lxml")
        index = div_bd.find_all('div', class_='block bd')
        name_novles = BeautifulSoup(str(index[1]), "lxml")
        name = name_novles.find_all('a')
        self.index = len(name)
        print('排名数：', self.index, self.index_urls)
        for i in name:
            self.index_urls.append(self.url + i.get('href'))

    # 爬取目录 保存章节名与章节地址
    def download_urls(self, target):
        req = requests.get(url=target)
        html = req.text
        div_bf = BeautifulSoup(html, "lxml")
        name = div_bf.find_all('h2')
        self.novels_name = name[0].string
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]), "lxml")
        a = a_bf.find_all('a')
        self.nums = len(a[12:])  # 剔除不必要的章节，并统计章节数
        for each in a[12:]:
            self.names.append(each.string)
            self.urls.append(self.url + each.get('href'))

    # 爬取章节内容
    def get_contents(self, target):
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html, "lxml")
        texts = bf.find_all('div', class_='showtxt')
        # 有的空4个字符有的空8个字符
        string = (str(texts[0])[34:].replace('<br/>', '\n'))
        split_str = string[0:4]
        if split_str.isspace():
            texts = texts[0].text.replace('\xa0' * 8, '\n\n    ')
            return texts
        else:
            return string

    # 保存章节名，章节内容
    def writer(self, name, path, text):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


# 非阻塞检测键盘输入 q+enter 返回true
def check_input():
    import select
    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        for line in sys.stdin:
            if line == 'q\n':
                return True
        return False
    else:
        return False


if __name__ == "__main__":
    dl = download()
    dl.get_url_list()
    for index in dl.index_urls:
        break_flag = False
        dl.download_urls(index)
        print('《%s》开始下载：' % dl.novels_name)
        save_name = dl.novels_name + '.txt'

        for i in range(dl.nums):
            break_flag = check_input()
            if(break_flag):
                break
            else:
                pass
            dl.writer(dl.names[i], save_name, dl.get_contents(dl.urls[i]))
            sys.stdout.write("  已下载:%2.3f%%" % float(i / dl.nums * 100) + '\r')
            sys.stdout.flush()
        if break_flag:
            print('《%s》下载中断' % dl.novels_name)
        else:
            print('《%s》下载完成' % dl.novels_name)
