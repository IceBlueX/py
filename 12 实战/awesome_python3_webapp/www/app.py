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
from jinja2 import Environment, FileSystemLoader

from orm_psql import *
from coroweb import *


def init_jinja2(app, **kw):
    logging.info('init jinja2...')
    options = dict(
        autoescape=kw.get('autoescape', True),
        block_start_string=kw.get('block_start_string', '{%'),
        block_end_string=kw.get('block_end_string', '%}'),
        variable_start_string=kw.get('variable_start_string', '{{'),
        variable_end_string=kw.get('variable_end_string', '}}'),
        auto_reload=kw.get('auto_reload', True)
    )
    path = kw.get('path', None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    logging.info('set jinja2 template path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options)
    filters = kw.get('filters', None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env


async def logger_factory(app, handler):
    async def logger(request):
        logging.info('Request: %s %s' % (request.method, request.path))
        # await asyncio.sleep(0.3)
        return(await handler(request))
    return logger





# 不同的请求 返回不同的路径
def index(request):
    return web.Response(body=b'<h1> Hello MYAwesomeWeb </h1>', content_type='text/html')  # 前面内容，后面类型


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000 ...')


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
