# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 9:13
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

# # 在Python中，1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高。
#
# # 切片 list列表、tuple元组、str字符串，都可以使用切片操作
# L = list(range(100))    # 用range创建序列，再用list转换为列表
# print(L[:3])            # L[0:3] - 从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。如第一个索引是0，可简写为L[:3]
# print(L[:10:2])         # L[:10:2] - 前10个数，每2个取一个
# print(L[::5])           # L[::5] - 所有数，每5个取一个
#
# T = tuple(range(100))
# print(T[:3])
# print(T[:10:2])
# print(T[::5])
#
# S = 'ABCDEFG'
# print(S[:3])
# print(S[::2])
#
# # 切片应用 字符串去首尾空格
# from trim import trim
# s = '    Hello World    '
# print(trim(s))
#
# # 迭代 for...in
# # 迭代dict时，默认遍历的是key，如果要获取value，for values in d.values()，如果要获取key和value，for k, v in d.items()
# d = {'a': 1, 'b': 2, 'c': 3}
#
# # 通过collections模块的Iterable类型判断
# from collections import Iterable
# print(isinstance(123, Iterable))   # isinstance() 用于判断一个变量是否是某种任务类型
#
# # enumerate() 函数将list转换为键值对
# for k, v in enumerate(['A', 'B', 'C']):
#     print(k, v)
#
# for x, y in [(1, 1), (2, 4)]:
#     print(x, y)
#
# # 列表生成式 把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
# print([x * x for x in range(1, 11)])
# print([m + n for m in 'ABC' for n in 'XYZ'])
# print([s.lower() for s in ['Hello', 'World', 'IBM']])
#
# # 引入os模块，使用os.listdir(path) 列出当前目录下的所有文件和目录名
# import os
# print([d for d in os.listdir('.')])

# # 生成器 在Python中，这种一边循环一边计算的机制，称为生成器：generator
# # 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
# g = (x * x for x in (range(10)))
# for n in g:
#     print(n)
#
# # 定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# # 生成器与普通函数的区别：普通函数调用直接返回结果，generator函数的“调用”实际返回一个generator对象

# 迭代器
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
from collections import Iterator
print(isinstance(iter('abc'), Iterator))
print(isinstance('abc', Iterator))