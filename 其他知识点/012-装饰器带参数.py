# -*- coding:utf-8 -*-


def check_login(func):
    def wrapper(name, passwd):
        if passwd == 12345 and name == 'zhangfei':
            return func(name, passwd)
        else:
            print('密码输入错误')
    return wrapper


@check_login
def login(name, passwd):
    print('%s登陆成功了,他的登录密码是%d' % (name, passwd))
    return 'hello'


login('zhangfei', 12345)
name = login('zhangfei', 12345)
print(name)
