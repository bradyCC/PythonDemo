# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 17:57
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : dict.py
# @Software: PyCharm

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

