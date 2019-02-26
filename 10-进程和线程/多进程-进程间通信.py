### mutiprocessing模块提供了queue，pipes等多种方式来交换数据

# 以queue为例，在两个进程中读写数据
from multiprocessing import Process, Queue 
import os, time, random

# 写数据进程
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程
def read(q):
    print('Process to read: %s' % os.getpgid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    #父进程创建Queue,并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    print(1)
    pr = Process(target=read, args=(q,))
    print(2)
    # 启动子进程pw写入
    pw.start()
    print(3)
    # 启动子进程pr读取
    pr.start()
    print(4)
    # 等待pw结束
    pw.join()
    print(5)
    # pr进程里是死循环，无法等待其结束，只能强行中止
    pr.terminate()
    print(6)