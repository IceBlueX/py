# 除法中的0除错误
# int 可能会抛出 ValueError
try :
    print('try...')
    r = 10/int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

#Python的错误其实也是class
#所有的错误类型都继承自BaseException
#所以在使用except时，它不但捕获该类型的错误，还捕获其子类类型的错误

#例
def foo():
    pass

try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')

#第二个except永远也捕获不到UnicodeError,
#因为UnicodeError是ValueError的子类
#即便有错误，也会被第一个except捕捉到

#常见的错误类型和继承关系看这里：
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy

#可跨越多层调用
#因此只需要在合适的位置捕获错误即可，无需每层都捕获
#例
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
##

# 调用栈
# err.py
def foo(s):
    return 10 / int(s)

def bar(s):
    return print(foo(s) * 2)

def main():
    bar('1')

main()
##

#记录错误   使用logging
#err_logging.py
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('1')
    except Exception as e:
        logging.exception(e)

main()
print('END')
#同样是报错，但是程序打印完错误信息后会继续执行，并且正常退出
##

#抛出错误
#因为错误是class
#捕获一个错误就是捕获到该class的一个实例
#因此，错误并不是凭空产生的，而是有意创建并抛出的
#可以根据需要，选好继承关系，自己定义一个错误的class
# err_raise.py
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('1')

#另一种错误处理方式
# err_reraise.py

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('1')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
##

#在bar()函数中，我们明明已经捕获了错误
#在打印了ValueError后，又把错误通过Raise语句抛出去了
#捕获错误目的只是为了记录一下，便于后续跟踪
#但是当前函数并不知道该如何处理该错误，因此会不断向上抛出，知道问题解决或报错

#raise也可以在except中进行错误类型转换，要注意逻辑合理
#例
try:
    10 / 1
except ZeroDivisionError:               #捕捉错误
    raise ValueError('input error!')    #转换错误类型
##
