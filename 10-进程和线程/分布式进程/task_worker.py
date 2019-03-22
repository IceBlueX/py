# 子程序

import time, sys, queue
from multiprocessing.managers import BaseManager


# 创建类似QueueManager:
class QueueManager(BaseManager):
    pass


# 只获取Queue, 所以只提供名字：
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是master机器
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码要和主程序一样
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接
m.connect()

# 获取queue对象
task = m.get_task_queue()
result = m.get_result_queue()

# 从task队列取任务，再把结果写进result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print ('task queue is empty.')

# 处理结束
print('worker exit.')
