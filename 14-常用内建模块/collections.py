#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LBK'

"""
 collections 集合类相关
"""
#
#
#
# ------------------- namedtuple 自定义名称tuple 可设定固定的变量个数 是tuple 的子集 -------------------
from collections import namedtuple

# ------ 定义点类型 ------
Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)

print(p.x, p.y)

# ------ 定义圆类型 包括圆心坐标及半径 ------
Circle = namedtuple('Circle', ['x', 'y', 'r'])

#
#
#
# ------------------- deque 高效实现插入和删除的双向列表 适合用于队列和栈 -------------------
from collections import deque

q = deque(['a', 'b', 'c'])

q.append('x')  # 从尾部插入数据
q.appendleft('y')  # 从头部插入数据

print(q)


#
#
# ------------------- defaultdict 当key不存在时，会返回已设定的默认值 -------------------
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')  # 设定默认值
dd['key1'] = 'abc'

print(dd['key1'], dd['key2'])  # 同时调用存在的key 和 不存在的key 不存在的值返回'N/A'

#
#
# ------------------- OrderedDict key不再是无序的，而是按照插入的顺序排序 -------------------
from collections import OrderedDict

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3

print(list(od.keys()))  # >>>['z', 'y', 'x']

# ------ FIFO 先进先出 ------
# OrderedDict可以用来实现一个FIFO的dict, 当容量超出限制时，先删除最早添加的KEY


class LastUpdatedOrderedDict(OrderedDict):

    # 获得容量参数，初始化
    def __init__(self, capacity):

        # 直接super 调用超类（父类）的初始化函数初始化
        super(LastUpdatedOrderedDict, self).__init__()

        # 初始化参数中添加容量
        self._capacity = capacity

    def __setitem__(self, key, value):

        # 先判断 key 是否已经存在
        containskey = 1 if key in self else 0

        # 判断该容器是否已满 满则删除最先插入的
        if len(self) - containskey >= self._capacity:
            last = self.popitem(last=False)  # False 表示删除最先插入的数据
            print("remove: ", last)

        # key已存在则调整顺序 不存在则插入新的
        if containskey:
            del self[key]
            print('set: ', (key, value))

        else:
            print("add：", (key, value))
        # 调用父类方法
        OrderedDict.__setitem__(self, key, value)


#
#
# ------------------- ChainMap 将一组dict组成一个dict 可按照先后顺序在其中寻找参数 -------------------
from collections import ChainMap

# 应用程序往往需要传入参数，参数可以通过命令行传入，通过环境变量， 或者通过默认参数
# 可以用ChainMap实现参数的优先级查找

# ------ 查找 user 和 color 这两个参数 ------
import os
import argparse  # 命令行参数解析模块

# 构造 缺省 参数：
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()

command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 组合成chainMap: 依次为命令行  环境变量  默认参数
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数：
print('corlor = %s' % combined['color'])
print('user = %s' % combined['user'])


#
#
# ------------------- Counter 将一组dict组成一个dict 可按照先后顺序在其中寻找参数 -------------------
from collections import Counter

c = Counter()
for ch in 'shopping':
    c[ch] = c[ch] + 1

print(c)

