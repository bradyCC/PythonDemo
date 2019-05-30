# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 17:35
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : codecs.py
# @Software: PyCharm

# 文件操作
import codecs

f = codecs.open('t.txt', 'r', 'utf-8')      # 读取文件中的内容，返回list
lines = [line.strip() for line in f]
f.close()
print(lines)

f1 = codecs.open('t1.txt', 'w', 'utf-8')    # 将内容写入文件中
f1.write('Hello World!\n')
f1.write('Hello')
f1.close()