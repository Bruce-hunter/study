# -*- coding:utf-8 -*-

import redis

try:
    r = redis.StrictRedis(host='39.107.119.157', port=6379, db=1)
except Exception as e:
    print(e)
r.set('name', 'hello')
