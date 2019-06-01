# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 10:04
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : json.py
# @Software: PyCharm

# 解析JSON
import json

s = '{"firstName":"Michael","lastName":"Jordan"}'
d = {
    "firstName": "Michael",
    "lastName":"Jordan"
}
print(json.loads(s))
print(json.dumps(d))