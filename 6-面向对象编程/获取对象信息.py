#使用type()  返回对应的Class类型

print(type(123))            #基本类型
print(type('str'))

print(type(abs))            #函数或类
print(type(type(123)))

print(type(123)==type(123)) #判断基本类型
print(type(123)==int)

import types                #判断一个对象是否为函数

def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

#使用isinstance()

class Animal(object):       #判断是否为类
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a=Animal()
d=Dog()
h=Husky()

print(isinstance(h,Husky))
print(isinstance(h,Dog))
print(isinstance(h,Animal))
print(isinstance(d,Husky))

print(isinstance('a',str))  #也可用来判断基本类型
print(isinstance(123,str))
print(isinstance(b'a',str))

print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))

#使用dir()

print(dir('ABC'))           #获得所有属性和方法

print(len('ABC'))           #等价
print('ABC'.__len__())

class Myobject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj=Myobject()

print(hasattr(obj,'x'))     #有属性x吗  #获取基本类型属性

setattr(obj,'y',19)         #设置一个y

print(getattr(obj,'y'))     #获取属性y

print(hasattr(obj,'power')) #有方法power吗  #获取对象方法属性

print(getattr(obj,'power')) #获取属性power












