# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 16:18
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : test3.py
# @Software: PyCharm

import turtle
import time

turtle.pensize(2)
turtle.bgcolor('black')
colors = ['red', 'yellow', 'purple', 'blue']
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x%4])
    turtle.left(91)
turtle.tracer(True)
time.sleep(3)