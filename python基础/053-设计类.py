# -*- coding:utf-8 -*-


class Car(object):
    def run(self):
        print('小汽车正在跑')

    def stop(self):
        print('小汽车停车了')


class LanShen(Car):
    def sit(self):
        print('小汽车坐了5个人')


# def select(money):
#     if money > 1000000:
#         car = LanShen()
#     else:
#         car = JiGuang()
#     return car


class CarFactory(object):
    def create(self, money):
        if money > 1000000:
            car = LanShen()
        else:
            car = JiGuang()
        return car


class JiGuang(Car):
    def sit(self):
        print('小汽车坐了3个人')


class CarStore(object):
    def order(self, money):
        return CarFactory().create(money)



car = CarStore()
car.order(1000000000000).sit()



