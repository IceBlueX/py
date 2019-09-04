#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LBK'

"""
本地默认配置文件
"""

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 5432,
        'user': 'libaokun',
        'password': 'password',
        'database': 'test',
    },
    'session': {
        'secret': 'Awesome'
    }
}


