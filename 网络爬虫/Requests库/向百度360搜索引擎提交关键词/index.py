# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 16:35
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

# https://www.baidu.com/s?wd=keyword  百度关键词搜索接口
# https://www.so.com/s?q=keyword  360关键词搜索接口

import requests


def getHTMLText(url, kv):
    try:
        r = requests.get(url, params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.request.url)
        print(len(r.text))
        return r.text
    except IOError:
        print('爬取失败')


if __name__ == '__main__':
    # 百度
    # url = 'http://www.baidu.com/s'
    # kv = {'wd': 'Python'}

    # 360
    url = 'http://www.so.com/s'
    kv = {'q': 'Javascript'}

    print(getHTMLText(url, kv))
