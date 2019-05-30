# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 17:06
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

import re

r = re.search(r'[1-9]\d{5}', 'BIT 100081').group(0)           # re.search() 匹配后返回match对象，使用match.group(0)获取
r = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')          # re.findall() 匹配后返回list
r = re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084')  # re.sub() 执行匹配字符串替换