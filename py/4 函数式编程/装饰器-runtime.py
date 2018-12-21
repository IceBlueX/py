import functools
import time 
import datetime

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        print('%s executed in %s ms' % (fn.__name__, time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))))
        print('%s executed in %s ms' % (fn.__name__, datetime.datetime.now()))
        return fn(*args,**kw)
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
print(f)
s = slow(11, 22, 33)
print(s)


if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
