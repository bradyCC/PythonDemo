# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 16:14
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : turtle1.py.py
# @Software: PyCharm

import turtle
import time

turtle.speed('fastest')
turtle.pensize(2)
for x in range(100):
    turtle.forward(2*x)
    turtle.left(90)
time.sleep(3)