# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 16:21
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

import requests


def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except IOError:
        print('爬取失败')


if __name__ == '__main__':
    url = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
    print(getHTMLText(url))
