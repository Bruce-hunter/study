# -*- coding:utf-8 -*-

import pymongo

client = pymongo.MongoClient('39.107.119.157', '27017')
print(client)
print('---1---')

db = client.test3
print(db)
print('---2---')
stu = db.stu
print(stu)
print('---3---')
s = stu.find()
print('---4---')
print(s.__next__())
print(s.__next__())
print(s.__next__())



