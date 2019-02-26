#subprocess 启动子进程，并控制其输入输出

###
import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit Code: ', r)

###输入则通过communicate()方法
#相当于执行命令nslookup再输入
#set q=mx
#python.org
#exit
print('\n$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code: ', p.returncode)
