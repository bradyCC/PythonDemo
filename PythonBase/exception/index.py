# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 13:56
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

# 异常处理机制 高级语言通常都内置了一套try...except...finally...的错误处理机制

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar(0)
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')