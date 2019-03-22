# 主程 from: 2019-02-26 15:25:23

import random,time,queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接受结果的队列
result_queue = queue.Queue()


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


# 把两个Queue都注册到网络上，callable参数关联了Queue对象：
QueueManager.register('get_task_queue', callable=lambda:task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000， 设置验证码’abc‘:
manager = QueueManager(address=('', 5000), authkey= b'abc')
print(1)
# 启动Queue：
manager.start()
print(2)
# 获得通过网络访问的Queue对象：
task = manager.get_task_queue()
result = manager.get_result_queue()
print(3)
# 放任务进去
for i in range(10):
    n = random.randint(0,10000)
    print('Put task %d...' % n)
    task.put(n)

print(4)
# 从result队列读取结果：
print('Try get results...')
print(5)
for i in range(10):
    r = result.get(timeout=100)
    print('Result: %s' % r)
print(6)
# 关闭u
manager.shutdown()
print('master exit.')

