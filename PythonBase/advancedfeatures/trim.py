# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 9:27
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : trim.py
# @Software: PyCharm

# 切片 - 去除字符串首尾空格
def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])

