# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 17:38
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : processControl.py
# @Software: PyCharm

# 条件判断 if...elif...else
birthday = input('Please enter your birthday year: ')
if len(birthday) != 4:
    print('请输入四位年份')
elif 1980 <= int(birthday) < 1990:
    print('80后')
elif 1990 <= int(birthday) < 2000:
    print('90后')
elif 2000 <= int(birthday) < 2010:
    print('00后')
elif int(birthday) >= 2010 :
    print('10后')
else:
    print('大龄青年')

# Python中循环有两种： 1- for...in   2-while
# Python提供了 range() 函数 用于生产一个整数序列，再通过 list() 函数转换为list  例如：range(5) - [0,1,2,3,4]
# 在循环中，break语句可以提前退出循环，continue语句可以跳过当前循环
sum = 0
for x in range(101):
    sum = sum + x
print(sum)



