# -*- coding:utf-8 -*-


# 定义人的类
class Person(object):
    def __init__(self, name):
        self.gun = None
        self.name = name
        self.hp = 100

    def __str__(self):
        if self.gun:
            msg = '当前的持枪人是%s,手上拿的枪是%s，他的血量是%d' % (self.name, self.gun.name, self.hp)
        else:
            msg = '受枪伤得人是%s,他的血量是%d' % (self.name, self.hp)
        return msg

    # 人能够装子弹
    def load_bullet(self, bullet, danjia):
        danjia.save_bullet(bullet)

    # 人能够安装弹夹
    def load_danjia(self, danjia, gun):
        gun.save_danjia(danjia)

    # 人能够拿起枪来
    def hand_gun(self, gun):
        self.gun = gun

    # 人能够开枪射击
    def shotting(self, person):
        self.gun.shot(person)

    # 人掉血
    def diaoxue(self,damage):
        if self.hp > 0:
            self.hp -= damage
        else:
            print('人已经死透了')


# 定义枪的类
class Gun(object):
    def __init__(self, name):
        self.name = name
        self.danjia = None

    def __str__(self):
        return '枪里还有%d颗子弹' % len(self.danjia.num)

    # 枪能够保存弹夹
    def save_danjia(self, danjia):
        if not self.danjia:
            self.danjia = danjia
        else:
            print('枪的上面已经装上了弹夹')

    # 枪能够射出子弹
    def shot(self, person):
        bullet = self.danjia.pop_bullet()
        if bullet:
            bullet.hurt(person)
        else:
            print('你的枪里没有子弹')


# 定义弹夹的类
class DanJia(object):
    def __init__(self, contain=30):
        self.contain = contain
        self.num = []

    # 弹夹能够保存子弹
    def save_bullet(self, bullet):
        # if len(self.num) == 0:
        #     self.num.append(bullet)
        # elif len(self.num) < self.contain:
        #     if bullet not in self.num:
        #         self.num.append(bullet)
        #     else:
        #         print('装入了同一颗子弹')
        if len(self.num) < self.contain:
            self.num.append(bullet)
        else:
            print('你的弹夹已经装满了子弹')

    # 弹夹能够弹出子弹
    def pop_bullet(self):
        if len(self.num) > 0:
            bullet = self.num[-1]
            self.num.pop()
            return bullet
        else:
            return None


# 定义子弹的类
class Bullet(object):
    def __init__(self):
        self.damage = 10

    # 子弹有伤害的方法
    def hurt(self, person):
        person.diaoxue(self.damage)


bullet = Bullet()
danjia = DanJia()
gun = Gun('AK47')
laowang = Person('lawang')
laozhang = Person('laozhang')
print(laowang)
print(laozhang)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_bullet(bullet, danjia)
laowang.load_danjia(danjia, gun)
laowang.hand_gun(gun)
laowang.shotting(laozhang)
print(laozhang)
print(laowang)
laowang.shotting(laozhang)
print(laozhang)
print(laowang)
laowang.shotting(laozhang)
print(laozhang)
print(laowang)
laowang.shotting(laozhang)
print(laozhang)
print(laowang)
laowang.shotting(laozhang)
print(laozhang)
print(laowang)
laowang.shotting(laozhang)
print(laozhang)
print(laowang)
laowang.shotting(laozhang)
print(laozhang)
print(laowang)
laowang.shotting(laozhang)
print(laozhang)
print(laowang)
laowang.shotting(laozhang)
print(laozhang)
print(laowang)
laowang.shotting(laozhang)
print(laozhang)
print(laowang)
laowang.shotting(laozhang)
print(laozhang)
print(laowang)
laowang.shotting(laozhang)
print(laozhang)
print(laowang)