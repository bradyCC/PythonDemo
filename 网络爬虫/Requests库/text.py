# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 11:36
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : text.py
# @Software: PyCharm

import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except IOError:
        print('爬取异常')


if __name__ == '__main__':
    url = 'http://www.bilibili.com'
    print(getHTMLText(url))