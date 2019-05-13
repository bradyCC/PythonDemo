# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 17:40
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

import requests


def getAttribution(url, kv):
    try:
        r = requests.get(url, params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:-500]
    except IOError:
        print('爬取失败')

if __name__ == '__main__':
    url = 'http://www.ip138.com/ips138.asp'
    kv = {'ip': '192.168.1.119', 'action': '2'}

    print(getAttribution(url, kv))