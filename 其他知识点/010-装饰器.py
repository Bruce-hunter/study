# -*- coding:utf-8 -*-


def check_login(func):
    def login():
        passwd = input('请输入密码:')
        if passwd == '12345':
            func()
        else:
            print('密码输入错误')
    return login


@check_login
# login_on = check_login(login_on)
def login_on():
    print('登陆成功了')


login_on()
