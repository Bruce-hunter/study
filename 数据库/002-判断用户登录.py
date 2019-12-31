# -*- coding:utf-8 -*-

import sys
import MysqlConn
import hashlib

flag = 0


def main():
    while True:
        global flag
        if flag == 0:
            name = input('请输入你的用户名:')
            passwd = input('请输入密码:')
        s = hashlib.sha1()
        s.update(passwd.encode('utf-8'))
        new_passwd = s.hexdigest()
        mysql = MysqlConn.MysqlHelper('39.107.119.157', 3306, 'test3', 'dxl', '123456')
        data = mysql.get_one('select passwd from userinfo where name=%s', (name, ))
        if data:
            if data[0] == new_passwd:
                print('密码输入正确，登录完成')
                break
            else:
                print('你输入的密码不正确，请检查后重新输入')
                passwd = input('请输入密码:')
                flag += 1
                if flag >= 2:
                    sys.exit('你输入的密码次数已经超限，请稍后重试')
        else:
            print('抱歉，没有该用户名，请重新输入')


if __name__ == '__main__':
    main()
