# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 21:25
# @Author  : brady
# @Email   : acheng_@163.com
# @File    : re.py
# @Software: PyCharm

import re

# secret_code = 'adfadfasdfaxxIxxadfasdfaw13123xxLovexx123134aadfdsfasxxYouxxadfasdf2123'
#
# b = re.findall('xx(.*?)xx', secret_code)
# print(b)
# c = re.search('xx(.*?)xx', secret_code).group(1)
# print(c)
# d = re.sub('xx(.*?)xx', '999999', secret_code)
# print(d)
# e = re.findall('(\d+)', secret_code)
# print(e)

old_url = 'http://www.jikexueyuan.com/course/android/?pageNum=2'
total_page = 20

# f = open('text.html', 'r')
# html = f.read()
# f.close()

# title = re.search('<title>(.*?)</title>', html, re.S).group(1)
# print(title)
# links = re.findall('href="(.*?)"', html, re.S)
# print(links)

# 替换连接 - 实现翻页功能
for i in range(2, total_page+1):
    new_link = re.sub('pageNum=\d+', 'pageNum=%d' % i, old_url, re.S)
    print(new_link)
