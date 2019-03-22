#Python多线程由于GIL的问题只能跑在一个CPU核心上，不能跑满核心
#要想跑满核心只能用多进程

#死循环测试，CPU占用最多100% 达不到400%
import threading,multiprocessing

def loop():
    x = 0
    while True:
        x = x^1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()

