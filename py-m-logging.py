#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LBK'

"""
    logging 模块简介
    logging 代替 print在程序中打印信息
    可以很方便的控制打印信息的等级
    在debug时十分方便
    
    logging.basicConfig函数各参数：
        filename：指定日志文件名；
        filemode：和file函数意义相同，指定日志文件的打开模式，'w'或者'a'；
        datefmt：指定时间格式，同time.strftime()；
        level：设置日志级别，默认为logging.WARNNING；
        stream：指定将日志的输出流，可以指定输出到sys.stderr，sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略；
        format：指定输出的格式和内容，format可以输出很多有用的信息
            %(levelno)s：打印日志级别的数值
            %(levelname)s：打印日志级别的名称
            %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
            %(filename)s：打印当前执行程序名
            %(funcName)s：打印日志的当前函数
            %(lineno)d：打印日志的当前行号
            %(asctime)s：打印日志的时间
            %(thread)d：打印线程ID
            %(threadName)s：打印线程名称
            %(process)d：打印进程ID
            %(message)s：打印日志信息
"""
import logging

DEBUG = False

if DEBUG:
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
else:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.info("Start print log")
logging.debug("Do something debug")
logging.warning("Someting maybe fail.")
logging.info("Finish")




