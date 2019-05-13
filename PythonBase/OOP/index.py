# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 11:36
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : index.py
# @Software: PyCharm

# type() 判断类型
# isinstance() 判断一个对象是否为某种类型的实例化对象
# dir(obj) 获取对象的所有属性和方法
# len(obj) 获取对象的长度
# hasattr(obj, property) 判断对象是否函数某种属性
# getattr(obj, property) 获取对象的某种属性
# setattr(obj, property, value) 设置对象的某种属性

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    def __iter__(self):
        return self

    def __call__(self):
        print('My name is %s' % self.name)

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


s = Student('Brady', 89)