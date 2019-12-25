# -*— coding:utf-8 -*-


def get_num(func, b, a):
    result = func(a)
    print(result)


fun = lambda x: x
get_num(fun, a=[2, 3, 4, 5], b=5)


dic = [dict(name='laowang', age=18, hobby='football'), dict(name='laozhang', age=16, hobby='basketball'), dict(name='laoli', age=15, hobby='football')]
dic.sort(key=lambda x: x['age'])
print(dic)