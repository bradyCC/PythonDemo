# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 14:15
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : test3.py
# @Software: PyCharm

# name = input('please enter your name: ')
# print('Hello,', name)

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5, 2))
