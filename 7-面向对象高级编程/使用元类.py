# type() 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的

from hello import Hello

h = Hello()
h.hello()

print(type(Hello)) #class 类型为 type  type()可以查看类型
print(type(h))     #实例 类型为class


#type() 还可以根据类型创建新的类型

def fn(self, name = 'world'): #先定义函数
    print( 'Hello, %s.' % name)

Hello0 = type('Hello0',(object,), dict(hello = fn)) # 创建Hello class

h0 = Hello0()
h0.hello()

print(type(Hello0)) #class 类型为 type  type()可以查看类型
print(type(h0))     #实例 类型为class

#要创建一个class对象  type（）依次传入三个参数：
#1. class的名称
#2. 继承的父类集合，注意python 支持多重继承，如果只有一个父类，别忘了tuple的单元素写法
#class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上


#使用元类metaclass创建类
#与先创建类再创建实例相同，先定义元类就可以动态创建类
#因此先创建元类，再动态创建类，再动态创建实例

#metaclass是类的模板，所以必须从’type‘类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass = ListMetaclass):
    pass

#__new__()方法接收到的参数依次是
#1.当前准备创建的类的对象
#2.类的名字
#3.类继承的父类集合
#4.类的方法集合

L = MyList()

L.add(1)

print(L)







