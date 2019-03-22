# ThreadLocal是一个全局的dict用来存放所有的某类对象，
# 然后用thread自身作为Key来获取相应的对象

import threading

# 创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    #获取当前线程关联的student:
    std = local_school.student 
    print('Hello, %s (in %s)\n' % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args= ('Alice',), name= 'Thread-A')
t2 = threading.Thread(target= process_thread, args= ('Bob',), name= 'Thread-B')

t1.start()
t2.start()

t1.join()
t2.join()



