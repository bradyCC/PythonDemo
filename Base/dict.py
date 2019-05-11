# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 17:57
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : dict.py
# @Software: PyCharm

# Python中判断key是否存在的方法有两种： 1- key in dist  2- d.get(key)
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael'] = 80                            # 赋值
print(d['Michael'])
d.pop('Bob')                                 # 删除
print(d)




