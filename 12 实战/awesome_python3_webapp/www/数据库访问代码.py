#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LBK'

"""
测试数据库是否连接正常
同时ORM框架是否可用
"""

import orm_psql
from models import User, Blog, Comment

import asyncio
import random


async def link(loop):
    await orm_psql.create_pool(loop, user='libaokun', password='password', database='test')

    u = User(name='Test', email='test%s@example.com' % random.randint(0, 10000000), passwd='1234567890', image='about:blank')
    users = await User.findAll()
    print(users)
    await u.save()


# 要运行协程，需要使用事件循环
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(link(loop))
    print('Test finished.')
    loop.close()

# def test():
#     yield from orm.create_pool('libaokun', password='password', database='test')
#
#     u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
#
#     yield from u.save()
#
#
# for x in test():
#     pass








