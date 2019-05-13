# -*- coding: utf-8 -*-
# @Time    : 2019-05-12 21:13
# @Author  : brady
# @Email   : acheng_@163.com
# @File    : power.py
# @Software: PyCharm

def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5, 3))