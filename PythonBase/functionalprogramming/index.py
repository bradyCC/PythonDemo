# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 10:33
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

# # 高阶函数 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
# f = abs
#
# def add(x, y, f):
#     return f(x) + f(y)
#
# print(add(-3, 6, f))

# # map() 函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# # reduce() 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#
# def mult(x):
#     return x * x
#
# r = map(mult, [1, 2, 3, 4])
# print(list(r))
# print(list(map(str, [1, 2, 3, 4, 5])))
#
# from functools import reduce
# def fn(x, y):
#     return x * 10 + y
#
# print(reduce(fn, [1, 3, 5, 7, 9]))

# # filter() 函数用于过滤序列。和map()不同的是，把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#
# def is_odd(n):
#     return n % 2 == 1
#
# print(list(filter(is_odd, [1, 2, 3, 4, 5])))
#
# def not_empty(s):
#     return s and s.strip()
#
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# sorted() 函数可以对list进行排序，它还可以接收一个key函数来实现自定义的排序，可以传入第三个参数reverse=True 进行反向排序
# print(sorted([36, 5, -12, 9, -21], key = abs, reverse = True))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))


# # 匿名函数 关键词lambda表示匿名函数，冒号前面的x表示函数参数。
# # 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# f = lambda x: x * x
# print(f(2))

# 装饰器 待研究
# 偏函数 待研究
