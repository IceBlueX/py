#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LBK'

"""
处理URL
"""

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id


@get('/')
async def index(request):
    users = await User.findAll()
    print('在 handlers.py->index中 根据路径获得后端返回的数据', users)
    # for u in users:
    #     print(u.name, u.email)
    return {
        '__template__': 'test.html',
        'users': users
    }


