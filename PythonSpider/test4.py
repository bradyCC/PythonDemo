# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 15:54
# @Author  : Brady
# @Email   : acheng_69@163.com
# @File    : test4.py
# @Software: PyCharm

import pymongo

conncetion = pymongo.MongoClient()
db = conncetion.MyMongo
table = db.test

data1 = {'name': 'Brady', 'age': '32', 'skill': 'Python'}
data2 = {'name': 'Lucy', 'age': '24', 'skill': 'PHP', 'other': '这里是其他备注信息'}
data3 = {'name': 'Lily', 'age': '22', 'other': '这里也是备注信息'}
# table.insert_one(data1)  # 插入数据 使用insert_one 或 insert_many, insert已废弃
# table.insert_many([data1, data2])
# table.insert_one(data3)
# table.delete_one({'name': 'Brady'})  # 删除数据 使用delete_one 或 delete_many, remove已废弃
# table.delete_many({})

print('操作数据库完成')
