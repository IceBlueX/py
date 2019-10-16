# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LBK'

"""
 协程 Coroutine
 consumer 是一个 生成器 一直在循环中通过 yield接收数据 并打印 又通过yield传回
 先调用c.send(None)启动生成器
 终止条件在produce中
 
"""


def consumer():
    r = ''
    while True:
        n = yield r  # 接收的值为n 并将r的值传出
        if not n:
            print("QUIT")
            return
        print('[CONSUMER] Consuming %s......' % n)
        r = '200 OK'


def produce(c):
    # 在使用c.send(n)之前，必须先使用c.send(None)或next(c)来返回生成器中的第一个值
    # 即先初始化 以启动生成器函数
    c.send(None)    # 相当于next(c) 用于接收c中下一个yield返回的值

    n = 0   # 初始条件
    while n < 5:       # 循环 及 结束条件
        n = n + 1       # 循环递增
        print('[PRODUCER] Producing %s......' % n)
        r = c.send(n)  # 接收下一个r 并将n传出
        print('[PRODUCER] Consumer return: %s......' % r)
    c.close()  # 满足结束条件后 退出协程


C = consumer()
produce(C)











