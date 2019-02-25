#JSON 进阶 类的序列化
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

#可选参数default就是把任意一个对象变成一个可序列为JSON的对象

### 函数转换
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
L = json.dumps(s, default = student2dict)
print("函数",json.dumps(s, default = student2dict))

### 利用__dict__函数 用来储存实变量的函数   但定义了__slots__的class不可用
print('__dict__',json.dumps(s, default = lambda obj:obj.__dict__))


# 反序列化
###函数转换
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
print(json.loads(L, object_hook=dict2student))
