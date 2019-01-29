# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 14:58
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态不是200, 则报异常
        r.encoding = r.apparent_encoding  # 解码: ISO-8859-1 转为 utf-8
        return r.text  # 返回网页内容
    except:
        return '产生异常'


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    print(getHTMLText(url))

