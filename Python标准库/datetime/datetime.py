# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 17:17
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : datetime.py
# @Software: PyCharm

# 日期和时间操作
from datetime import *

# now = datetime.now()            # datetime类：2019-05-30 17:30:33.682538
# now = date(2019, 5, 1)          # date类：默认需要传year、month、day
# now = date.today()              # 当日：格式为 2019-05-30
# now = time(12, 30, 0)           # time类：12:30:00

# 时间戳转换为指定格式的日期
timeStamp = 1551077515
timeArray = datetime.utcfromtimestamp(timeStamp)
formatTime = timeArray.strftime('%Y-%m-%d %H:%M:%S')
print(formatTime)
