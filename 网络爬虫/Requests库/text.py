# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 11:36
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : text.py
# @Software: PyCharm

import requests
import re

def getHTMLText(url):
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/74.0.3729.131 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        japanTitle = re.findall('color:#666666;"(.*?)</span>', r.text, re.S)
        for item in japanTitle:
            print(item)
        chineseTitle = re.findall('color: #039;"(.*?)</a>', r.text, re.S)
        for item in chineseTitle:
            print(item)
        # return r.text
    except IOError:
        print('爬取异常')


if __name__ == '__main__':
    url = 'http://jp.tingroom.com/yuedu/yd300p'
    print(getHTMLText(url))