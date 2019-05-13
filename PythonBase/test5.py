# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 10:04
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : test5.py
# @Software: PyCharm

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()

