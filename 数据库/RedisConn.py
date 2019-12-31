# -*- coding:utf-8 -*-

import redis


class RedisHelper(object):
    def __init__(self, host='localhost', port=6379, db=0):
        self.__redis = redis.StrictRedis(host, port, db)

    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ''

    def set(self, key, value):
        self.__redis.set(key, value)


if __name__ == '__main__':
    r = RedisHelper('39.107.119.157')
    print(r.get('name'))
