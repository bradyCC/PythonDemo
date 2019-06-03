# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 10:29
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

# 检测代理IP是否可用
import os

ip = [

]

arr = []

for item in ip:
    result = os.system("tcping " + item['ipCheck'])
    if result == 0:
        with open('ip.txt', 'a+') as f:
            f.write('"' + item['ipAddress'] + '",\n')
            f.close()
        arr.append(item['ipAddress'])

print(arr)
