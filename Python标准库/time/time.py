# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 17:58
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : time.py
# @Software: PyCharm

# 时间戳
import time

# print(time.time())

# 时间戳转换为指定格式的日期
timeStamp = 1551077515
timeArray = time.localtime(timeStamp)
formatTime = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
print(formatTime)
