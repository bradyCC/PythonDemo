# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 10:13
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : fib.py
# @Software: PyCharm

# 斐波拉契数列 除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
