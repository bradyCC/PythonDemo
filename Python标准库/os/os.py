# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 11:44
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

# 操作系统
import os

# os.getcwd()               # 当前工作目录
# os.mkdir('data')          # 创建文件夹
# os.rmdir('data')          # 删除文件夹
# os.path.exists('data')    # 判断文件是否存在

name = input('please enter your name: ')

if not os.path.exists('data.txt'):
    with open('data.txt', 'w') as f:
        f.write(name)
        f.close()
