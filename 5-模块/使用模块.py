#使用模块

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello,world!')
    elif len(args)==2:
        print('Hello %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

#作用域
def _private_1(name):
    return 'Hello, %s !' % name

def _private_2(name):
    return 'Hi, %s !' % name

def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)
print(greeting('MC'))
print(greeting('MCKY'))