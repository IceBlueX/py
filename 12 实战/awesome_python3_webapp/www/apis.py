#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LBK'

"""
JSON API 定义
"""

import json, logging, inspect, functools


class APIError(Exception):
    """
    这基础的APIError包括必需的error, 可选的data, 还有可选的message
    """
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(APIError):
    """
    指示输入值有错误或者无效，数据指定输入表单的错误字段
    """
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)


class APIResourceNotFoundError(APIError):

    """
    表示未找到资源，数据指定资源名称
    """
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)


class APIPermissionError(APIError):
    """
    表示API没有权限
    """
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)





