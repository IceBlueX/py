#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LBK'
'''
web app 骨架
可以监听请求 并相应相应的路由路径
'''

# 导入通知 通知级别设置
import logging;  logging.basicConfig(level=logging.INFO)

# 导入常用模块
import asyncio
import os
import json
import time

from datetime import datetime

from aiohttp import web


# 不同的请求 返回不同的路径
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000 ...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
