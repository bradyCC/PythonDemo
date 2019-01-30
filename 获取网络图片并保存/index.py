# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 17:01
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

import requests
import os

root = 'D://pics//'
url = 'http://picm.bbzhi.com/fengjingbizhi/alasijiahenanjizhoufeng/show_fengjingou_239550_m.jpg'
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except IOError:
    print('爬取失败')

