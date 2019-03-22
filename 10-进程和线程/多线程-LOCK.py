#多线程和多进程最大的不同在于，
#多个进程中，同一个变量在各个进程中互不影响、
#而多线程中，所有变量由所有线程共享  因此变量容易被改乱

#改乱 例
import time,threading

balance = 0 #假定为银行存款
lock = threading.Lock() #锁声明定义


def change_it(n):
    #先存后取，结果一般为0
    global balance
    balance = balance + n
    balance = balance - n


#未修改
"""def run_thread(n):
    for i in range(1000000):
        change_it(n)"""

#修改后加锁，在某个线程修改此变量时，其他线程不能修改
#可用于保护重要数据的准确性
#但同时效率也会大大降低
def run_thread(n):
    for i in range(1000000):
        #先获取锁：
        lock.acquire()
        try:
            #这里可以放心改
            change_it(n)
        finally:
            # 改完一定要记得释放锁  不然变量会锁死
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()

t1.join()
t2.join()

print(balance)

#当循环次数过多会出现错误是因为相同的变量在两个公式中交替执行

