# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 15:34
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : base.py
# @Software: PyCharm

# 当字符串中很多字符都需要转义时，Python允许用 r'' 表示''内容的字符串默认不转义
print(r'\\\\t\\\\')

# 当字符串中有很多换行时，Python允许使用 ''' ''' 表示多行内容
print('''line1 
line2
line3''')

# 运算： and-与 or-或 not-非

# 空值 None

# 在Python中，有两种除法：1 - / 结果为浮点数 2 - // 结果为正数
print(9 / 3)
print(10 // 3)

# Python提供了 ord() 函数获取字符的整数表示， chr() 函数把编码转换为对应的字符
print(ord('A'))
print(chr(66))

# Python中字符串通过 encode() 方法可以编码为指定的bytes， 通过 decode() 方法把bytes转换为str，可以传入 errors='ignore' 忽略错误的字节
print('ABC'.encode('ascii'))
print(b'ABC'.decode('utf-8', errors='ignore'))

# Python提供了 len() 函数获取字符串的长度
print(len('中文'))
print(len('中文'.encode('utf-8')))

# Python中，采用 % 实现格式化字符串   %s-字符串替换 %d-整数替换 %f-浮点数替换 %x-十六进制整数替换  字符串里面的%是一个普通字符就需要转义，用%%来表示一个%
print('Hi, %s, you have $%d' % ('Brady', 10000))

# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%2d - %02d' % (3, 1))

# Python提供了 format() 函数 实现格式化字符串
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('Brady', 17.125))

# Python中，有一种数据类型是列表：list - 是一种有序的集合
a = ['Michael', 'Bob', 'Tracy']
a.append('Adam')                   # 添加
a.insert(1, 'Jack')                # 插入
a.pop(1)                           # 删除
print(len(a))
print(a)

# Python中，有一种数据类型是元祖：tuple - 一旦初始化就不能修改 tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
classmates = ('Michael', 'Bob', 'Tracy')

# Python中判断key是否存在的方法有两种： 1- key in dist  2- d.get(key)
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael'] = 80                            # 赋值
print(d['Michael'])
d.pop('Bob')                                 # 删除
print(d)

# set类似于dict，是一组key的集合，但不存储value，key值不能重复
s = set([1,2,3,3])
s.add(4)
s.remove(1)
print(s)
