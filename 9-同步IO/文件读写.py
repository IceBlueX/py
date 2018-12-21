###读文件
#
with open('/Users/libaokun/py/9-同步IO/test.txt','r') as f:
    L = f.read()
    print(L)
#
#调用read()会一次性读取文件的全部内容，容易爆内存
#为保险起见，可以反复调用read(size)方法
#readline()可以每次读取一行内容
#readlines()以此读取全部内容，并按行返回list
#
with open('/Users/libaokun/py/9-同步IO/test.txt','r') as f:
    L = f.readlines()
    for n in L:
        print(n.strip()) # 把末尾的’\n‘去掉
#


###file-like Object
#
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object
# 除了file外，还可以是内存的字节流，网络流，自定义流等
# file-like Object不要求从特定类继承，只要写个read()方法就可以
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲


###二进制文件
#
#要读取二进制文件，比如图片，视频等等，用’rb‘模式打开文件即可
f = open('/Users/libaokun/py/9-同步IO/test.png','rb')
print(f.read())
#


###字符编码
#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
#
with open('/Users/libaokun/py/9-同步IO/test0.txt','r',encoding = 'gbk', errors = 'ignore') as f:
    L = f.read()                                                        # ^^^接收errors参数，对应遇到错误后的处理方式
    print(L)                                                            # |||此处为忽略错误
#


###写文件
#
# ’w’ 文本写文件，会覆盖  ‘wb’ 覆盖写二进制文件 ‘a’ 追加模式写入
#要写入特定编码的文件，要给open函数传入encoding函数
#没有f.close()且未使用with，数据可能只有部分写入磁盘
with open('/Users/libaokun/py/9-同步IO/test1.txt','a') as f:
    f.write('Hello, world!')
#


###
###注意with 的使用


    
