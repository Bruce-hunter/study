# -*- coding:utf-8 -*-

flag = 0

class handle(object):
    def han(self):
        global flag
        flag += 1

h = handle()
h.han()
# print(h.flag)
print(flag)