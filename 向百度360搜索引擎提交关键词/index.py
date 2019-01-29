# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 16:35
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

# https://www.baidu.com/s?wd=keyword  百度关键词搜索接口
# https://www.so.com/s?q=keyword  360关键词搜索接口

import requests

# 百度
url = 'https://www.baidu.com/s'
key = 'wd'
keyword = 'Python'

# 360
# url = 'https://www.so.com/s'
# key = 'q'
# keyword = 'Javascript'

try:
    kv = {key: keyword}
    r = requests.get(url, params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')
