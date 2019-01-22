# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 14:15
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : test3.py
# @Software: PyCharm

# name = input('please enter your name: ')
# print('Hello,', name)

# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))
print(power(5, 3))

# 递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))
