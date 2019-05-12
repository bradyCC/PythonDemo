# -*- coding: utf-8 -*-
# @Time    : 2019-05-12 21:34
# @Author  : brady
# @Email   : acheng_@163.com
# @File    : fact.py
# @Software: PyCharm

def fact(n):
   return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
