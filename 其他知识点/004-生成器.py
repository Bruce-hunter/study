# -*- coding:utf-8 -*-
# x = []
# b = (x for x in range(10))
# print(x)
# print(b)
# for i in b:
#     print(i)


def test():
    i = 0
    while True:
        print('---1---')
        result = yield i
        print(result)
        print('---2---')
        i += 1
        if i >= 10:
            break


b = test()
print(b.__next__())
b.send('hahha')
print(b.__next__())
print(b.send(None))
print('='*50)
for i in b:
    print(i)
