# multiprocessing

# Unix/Linux/Mac操作系统提供了一个fork()系统调用
# 调用fork一次返回两次 子进程永远返回0，父进程返回子进程的ID
# 子进程通过getppid()函数拿到父进程的ID
# Python的os模块封装了常见的系统调用，包括fork

import os

print('Process(%s) start...' % os.getpid() )
# Only works on Unix/Linux/Mac
pid = os.fork()
if pid == 0:
    print('I am child process(%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I(%s) just created a child process(%s).' % (os.getpid(), pid))

