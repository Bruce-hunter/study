# -*- coding:utf-8 -*-

import pymysql

conn = pymysql.connect(host='39.107.119.157', user='dxl', passwd='123456', database='test3', port=3306, charset='utf8')
cursor1 = conn.cursor()
count = cursor1.execute('select * from booktest_areas')
print(cursor1.fetchall())
print(count)
conn.commit()
cursor1.close()
conn.close()