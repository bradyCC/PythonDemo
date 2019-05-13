# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 9:13
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

# 在Python中，1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高。

# 切片 list列表、tuple元组、str字符串，都可以使用切片操作
L = list(range(100))    # 用range创建序列，再用list转换为列表
print(L[:3])            # L[0:3] - 从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。如第一个索引是0，可简写为L[:3]
print(L[:10:2])         # L[:10:2] - 前10个数，每2个取一个
print(L[::5])           # L[::5] - 所有数，每5个取一个

T = tuple(range(100))
print(T[:3])
print(T[:10:2])
print(T[::5])

S = 'ABCDEFG'
print(S[:3])
print(S[::2])

# 切片应用 字符串去首尾空格
from trim import trim
s = '    Hello World    '
print(trim(s))

# 迭代 for...in
# 迭代dict时，默认遍历的是key，如果要获取value，for values in d.values()，如果要获取key和value，for k, v in d.items()
d = {'a': 1, 'b': 2, 'c': 3}

# 通过collections模块的Iterable类型判断
# from collections import Iterable
# print(isinstance(123, Iterable))

# enumerate() 函数将list转换为键值对
# for k, v in enumerate(['A', 'B', 'C']):
#     print(k, v)

# for x, y in [(1, 1), (2, 4)]:
#     print(x, y)