# pickling 序列化 从内存到磁盘

##Python中pickle模块用来实现序列化
import pickle
d = dict(name = 'Bob', age = 20, score = 88)
a = pickle.dumps(d) #dumps()将任意一个对象序列化为一个bytes,然后可以写入文件
print(a)

#也可以用dump直接写入文件
#f = open('./9-同步IO/dump.txt', 'wb')
#pickle.dump(d,f)
#f.close()

#再用load读取
f = open('./9-同步IO/dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)


##序列化为json或者xml  json编码为UTF-8
#JSON           Python
# {}            dict
# []            list
# "string"      str
# 123.456       int/float
# true/false    True/False
# null          None

#用json模块进行格式转换
import json
d = dict(name = 'Bob', age = 20, score = 88)
l = json.dumps(d)
print(l)

#也可以用dump直接写入文件
f = open('./9-同步IO/dump.json', 'w')
json.dump(d,f)
f.close()

#用loads()或者load()读取json为dic
c = json.loads(l)
print(c)