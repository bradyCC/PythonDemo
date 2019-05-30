# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 17:44
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : random.py
# @Software: PyCharm

# 随机数
import random

# print(random.random())      # 生成[0.0,1.0]之前的随机小数，如不设置seed，默认使用当前时间作为随机数种子
# random.seed(10)             # 设置随机数种子
# print(random.random())

list = ['1', '2', '3', '4']
c = random.choice(list)     # random.choice(List) 从list中随机选取一个
print(c)
random.shuffle(list)        # random.shuffle(list) 随机排序
print(list)
r = random.randint(10, 100) # random.randint(a, b) 生成[a,b]之间的随机整数
print(r)
u = random.uniform(10, 100) # random.uniform(a, b) 生成[a,b]之间的随机小数
print(u)