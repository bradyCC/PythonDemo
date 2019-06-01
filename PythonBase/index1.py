# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 15:17
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index1.py
# @Software: PyCharm

# 摄氏度与华氏度之间的转换 0°C = 32°F  100°C = 212°F
'''
转换公式：
C = (F - 32) / 1.8
F = C * 1.8 + 32
'''

val = input('请输入带温度符号表示的温度值（如32C）：')
if val[-1] in ['C', 'c']:
    f = 1.8 * float(val[0:-1]) + 32
    print('转换后的温度为：%.2fF'%f)
elif val[-1] in ['F', 'f']:
    c = (float(val[0:-1]) - 32) / 1.8
    print('转换后的温度为：%.2fC'%c)
else:
    print('输入有误')