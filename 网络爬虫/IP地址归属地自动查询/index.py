# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 17:40
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

import requests

url = 'http://www.ip138.com/ips138.asp'
kv = {'ip': '192.168.0.117', 'action': '2'}

try:
    r = requests.get(url, params=kv)
    print(r.request.url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except IOError:
    print('爬取失败')
