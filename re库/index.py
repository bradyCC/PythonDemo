# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 14:28
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

# 正则表达式

import re

# re.search()  在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象  re.search(pattern=, string=, flags=)
# re.match()   从一个字符串的开始位置起匹配正则表达式，返回match对象
# re.findall() 搜索字符串，以列表类型返回全部能匹配的子串
# re.split()   将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
# re.finditer()搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
# re.sub()     在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串

# flags: re.I忽略大小写 re.M全局匹配 re.S设置后可以使.匹配换行符

# match = re.search(r'[1-9]\d{5}', 'BIT 100081')
# if match:
#     print(match.group(0))


# ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')

# for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
#     if m:
#         print(m.group(0))

# s = re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084')


# 面向对象用法  re.compile(pattern, flags=0)
# regex = re.compile(r'[1-9]\d{5}')
# match = regex.search('BIT 100081')


# match对象的属性
# match.string   待匹配的文本
# match.re       匹配时使用的pattern对象（正则表达式）
# match.pos      正则表达式搜索文本的开始位置
# match.endpos   正则表达式搜索文本的结束位置

# match对象的方法
# match.group(0) 获得匹配后的字符串
# match.start()  匹配字符串在原始字符串的开始位置
# match.end()    匹配字符串在原始字符串的结束位置
# match.span()   返回(.start(), .end())


# 默认贪婪匹配
# match = re.search(r'PY.*N', 'PYANBNCNDN')
# match.group(0)  # PYANBNCNDN

# 最小匹配
# match = re.search(r'PY.*?N', 'PYANBNCNDN')
# match.group(0)  # PYAN

