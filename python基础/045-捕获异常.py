# -*- coding:utf-8 -*-

try:
    print('---1---')
    11/0
    print('---2---')
    # f = open('print.txt')
    # caonima
# except (ZeroDivisionError, FileNotFoundError) as result:
#     print('你就是错了, %s' %result)
except Exception as result:
    print(result)
else:
    print('无异常')
finally:
    print('结束程序')
