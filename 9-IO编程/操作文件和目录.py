# 操作系统

import os
print(os.name)      # 操作系统类型

print(os.uname())   # 操作系统详细信息

# 环境变量

print(os.environ)      # 所有环境变量

print(os.environ.get('PATH'))      # PATH环境变量

print(os.environ.get('x','default'))      # PATH环境变量

# 操作文件和目录
# 查看当前目录的绝对路径：
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来：
print(os.path.join('/Users/libaokun/py','test'))

# 然后创建一个目录
#os.mkdir('/Users/libaokun/py/test')

# 删掉一个目录
#os.rmdir('/Users/libaokun/py/test')


# 不需要目录和文件真实存在，只是对字符串进行操作
# 文件目录拆分
print(os.path.split('/Users/libaokun/py/test'))
# 得到文件扩展名
print(os.path.splitext('/Users/libaokun/py/README.md'))

#os.rename('./9-IO编程/test.txt','./9-IO编程/test.py')
#os.rename('./9-IO编程/test.py','./9-IO编程/test.txt')

# 创建文件
#with open('/Users/libaokun/py/9-IO编程/test11.txt','a') as f:
#    f.write('Hello, world!')
# 删除文件
#os.remove('./9-IO编程/test11.txt')

#shutil模块提供了copyfile()函数，可以复制文件

#利用Python特性
#列出当前目录下的所有目录
L=[x for x in os.listdir('.') if os.path.isdir(x)]
print(L)
#列出当前目录下某特定格式的文件 如‘.md’
L=[ x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.md' ]
print(L)