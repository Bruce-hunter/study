# -*- coding:utf-8 -*-


class Car(object):
    def run(self):
        print('小汽车正在跑')

    def stop(self):
        print('小汽车停车了')


class LanShen(Car):
    def sit(self):
        print('小汽车坐了5个人')


class JiGuang(Car):
    def sit(self):
        print('小汽车坐了3个人')


class CarFactory(object):
    def create(self, money):
        if money > 1000000:
            car = LanShen()
        else:
            car = JiGuang()
        return car


class CarStore(object):
    def order(self, type):
        return self.createcar(type)


class LuhuCarStore(CarStore):
    def createcar(self, type):
        self.fac = Factory()
        return self.fac.create(type)


class Factory(object):
    def create(self, type):
        self.type = type
        if self.type == 'lansheng':
            car = LanShen()
        else:
            car = JiGuang()
        return car


car = LuhuCarStore()
car.order('lansheng').sit()