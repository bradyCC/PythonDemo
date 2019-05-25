# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 9:17
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : text3.py
# @Software: PyCharm

import requests

def getHTMLText(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/74.0.3729.131 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        with open('text3.html', 'wb') as f:
            f.write(r.content)
            r.close()
        return r.text
    except IOError:
        print('爬取失败')


if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/6136918785'
    print(getHTMLText(url))