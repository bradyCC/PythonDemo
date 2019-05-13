# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 16:15
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

import requests


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except IOError:
        print('爬取失败')


if __name__ == '__main__':
    url = 'https://item.jd.com/2967929.html'
    print(getHTMLText(url))
