# -*- coding: utf-8 -*-
# @Time    : 2019-05-12 21:12
# @Author  : brady
# @Email   : acheng_@163.com
# @File    : move.py
# @Software: PyCharm

import math

def move (x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

r = move(100, 100, 60, math.pi / 6)
print(r)