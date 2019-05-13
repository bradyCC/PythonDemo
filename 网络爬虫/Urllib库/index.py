# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 14:08
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

# Urllib是Python提供的一个用于操作URL的模块，我们爬取网页的时候，经常需要用到这个库。
# urllib.request  请求模块
# urllib.error  异常处理模块
# urllib.parse  url解析模块
# urllib.robotparser  robots.txt解析模块

import urllib.request

file = urllib.request.urlopen('http://www.baidu.com')
data = file.read()
with open('./1.html', 'wb') as f:
    f.write(data)
    f.close()
