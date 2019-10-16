#
###内存中读写文件

##StringIO    仅用于str
#
from io import StringIO
f = StringIO()
f.write('hello')
f.write(',')
f.write('world!')
print(f.getvalue())
#
#可以用一个str初始化StringIO,然后像读文件一样读取：
f = StringIO('Hello! \nHi! \nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
#
#
#指针位置变化与影响
# 初始化，说明指针指向0
sio = StringIO('abc')
print(sio.getvalue())       #读取当前值
print(sio.tell())           #显示当前指针位置
#
# 写入字符d
sio.write('d')
print(sio.getvalue())       #读取当前值
print(sio.tell())           #显示当前指针位置  此时指针移动到d后面(0,1,2,3)中的1位置
#
# 移动指针到末尾
sio.seek(0,2)               #此处参数为（3）或者（0,2）  (0,2)是移动指针到字符串末尾
print(sio.getvalue())       #读取当前值
print(sio.tell())           #显示当前指针位置   此时指针移动到c后面(0,1,2,3)中的3位置
#
# 写入字符 e
sio.write('e')
print(sio.getvalue())       #读取当前值
print(sio.tell())           #显示当前指针位置
#
#
sio = StringIO("abcdefg")
print(sio.tell()) # 当前指针的位置为 0
sio.seek(0, 2)
sio.write("hij") # 如果追加到文件末尾，就需要将初始化后的指针从0移动到文件末尾
print(sio.tell())
print(sio.getvalue())
#


##BytesIO
#
#
from io import BytesIO
fq = BytesIO()
fq.write('中文'.encode('utf-8'))
print(fq.getvalue())
#
#
fd = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(fd.read())
#





