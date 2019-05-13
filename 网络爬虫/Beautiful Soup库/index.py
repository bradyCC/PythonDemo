# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 9:20
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

# 安装 python3 -m pip install beautifulsoup4
# 解析、遍历、维护DOM树的功能库

import requests
from bs4 import BeautifulSoup

url = 'http://python123.io/ws/demo.html'
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')  # 解析html
    tag = soup.body
    # 解析
    # print(tag.title)  # 获取title标签及内容
    # print(tag.parent.parent.name)  # 获取标签的祖先元素名字
    # print(tag.attrs)  # 获取标签的所有属性
    # print(tag.attrs['href'])  # 获取标签中的href属性值
    # print(type(tag))  # 获取标签的类型
    # print(type(tag.attrs))  # 获取标签中属性的类型
    # print(tag.string)  # 获取标签中的内容
    # print(type(tag.string))  # 获取标签中的内容类型
    # 遍历
    # for child in tag.contents:  # 下行遍历 .contents返回列表类型
    #     print(child)
    # for parent in soup.a.parents:  # 上行遍历 .parents返回当前节点的所有先辈节点
    #     if parent is None:
    #         print(parent)
    #     else:
    #         print(parent.name)
    # 平行遍历发生在同一个父节点下的各节点间
    # for sibling in soup.a.next_siblings:  # 平行遍历后续节点
    #     print(sibling)
    # for sibling in soup.a.previous_siblings:  # 平行遍历前续节点
    #     print(sibling)
    print(tag.prettify())  # HTML格式化
except IOError:
    print('爬取失败')
