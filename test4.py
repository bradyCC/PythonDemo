# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 11:46
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : test4.py
# @Software: PyCharm

# 题目1：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                print(i, j, k)

