# -*- coding:utf-8 -*-

import sys
import hashlib
import MysqlConn
import RedisConn


flag = 0
redis = RedisConn.RedisHelper('39.107.119.157', db=7)
mysql = MysqlConn.MysqlHelper('39.107.119.157', 3306, 'test3', 'dxl', '123456')

while True:
    # global flag
    if flag == 0:
        name = input('请输入你的用户名:')
        passwd = input('请输入密码:')
    s = hashlib.sha1()
    s.update(passwd.encode('utf-8'))
    new_passwd = s.hexdigest()
    if redis.get(name):
        print(new_passwd)
        print(name)
        password = redis.get(name).decode('utf-8')
        # print(password.decode('utf-8'))
        if password == new_passwd:
            print('登陆成功了')
            break
        else:
            print('密码不正确,请重新输入')
            if flag >= 2:
                sys.exit('你输入的密码次数已经超限')
            passwd = input('请输入密码:')
            flag += 1
    else:
        data = mysql.get_one('select passwd from userinfo where name=%s', (name, ))
        if data:
            if data[0] == new_passwd:
                print('密码输入正确，登录完成')
                redis.set(name, new_passwd)
                break
            else:
                print('你输入的密码不正确，请检查后重新输入')
                if flag >= 2:
                    sys.exit('你输入的密码次数已经超限，请稍后重试')
                passwd = input('请输入密码:')
                flag += 1
        else:
            print('抱歉，没有该用户名，请重新输入')
