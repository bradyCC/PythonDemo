# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 13:53
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : text2.py
# @Software: PyCharm

import requests
import re


def postHTMLText(url):
    headers = {'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/74.0.3729.131 Safari/537.36'}
    data = {
        'q': 'filter',
        'save': '1',
        'random_seed': '541',
        'page': '2'  # 设置page获取第二页数据
    }
    try:
        r = requests.post(url, headers=headers, data=data)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        title = re.findall('"card-title">(.*?)</div>', r.text, re.S)
        print(len(title))
        for item in title:
            print(item)
        # return r.text
    except IOError:
        print('爬取失败')


if __name__ == '__main__':
    url = 'https://www.crowdfunder.com'
    print(postHTMLText(url))
