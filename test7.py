# -*- coding:utf-8 -*-

# import gevent
# # from gevent import monkey
# # monkey.patch_all()
#
#
# def f(n):
#     for i in range(n):
#         print(gevent.getcurrent(), i)
#         # 用来模拟一个耗时操作，注意不是time模块中的sleep
#         # gevent.sleep(1)
#
#
# # print('---1---')
# # gevent.spawn(f, 5)
# # gevent.spawn(f, 5)
# # gevent.spawn(f, 5)
# # print('---2---')
#
#
# g1 = gevent.spawn(f, 5)
# g2 = gevent.spawn(f, 5)
# g3 = gevent.spawn(f, 5)
# gevent.joinall((g1, g2, g3))
import time
import gevent


def f(n):
    # time.sleep(1)
    for i in range(n):
        print(gevent.getcurrent(), i)
        # 用来模拟一个耗时操作，注意不是time模块中的sleep
        gevent.sleep(1)
        # time.sleep(2)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
print('===1===')
gevent.sleep(1)
print('----1----')
# g1.join()
print('----2----')
# g2.join()
print('----3----')
# g3.join()
print('----4----')
