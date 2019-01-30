# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 10:48
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
import re
# .find_all()简写为()

url = 'http://python123.io/ws/demo.html'
try:
    r = requests.get(url)
    r.raise_for_status()
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')
    # .find_all(name, attrs, recursive, string, **kwargs) 返回列表类型
    # name: 对标签名称的检索 可以传字符串'a',也可以传列表['a', 'p']
    # for link in soup.find_all('a'):
    #     print(link.attrs['href'])
    # attrs: 对标签属性值的检索 可以传字符串'course' 也可以传id='link1'
    # print(soup.find_all(id=re.compile('link')))
    # recursive: 是否对子孙全部检索 默认为True
    # print(soup.find_all('a', recursive=False))
    # string: 检索字符串
    # print(soup.find_all(string=re.compile('python')))
    # re正则表达式库
    for tag in soup.find_all(re.compile('b')):
        print(tag.name)  # 返回所有包含b的标签的名字
except:
    print('爬取失败')
