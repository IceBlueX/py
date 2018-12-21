# 1 simple
def log0(func):
    def wrapper(*args,**kw): #接受任意参数调用
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log0
def now0():
    print('2018-12-10')

now0()

# 2 just so so
def log1(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log1('execute')
def now1():
    print('2018-12-10')

now1()

# 3 a little 

import functools

def log2(func):
    @functools.wraps(func)
    def wrapper(*args,**kw): #接受任意参数调用
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log2
def now2():
    print('2018-12-10')

now2()

###

def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log3('execute')
def now3():
    print('2018-12-10')

now3()