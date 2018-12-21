class Student(object):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):      #使用print打印类返回的字符串 __repr__()为调试者服务
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

print(Student('Michael'))

#__iter__   该方法返回一个迭代对象，for循环会不断调用该迭代对象的__next__()方法拿到下一个值

#以斐波那契数列为例
class Fib(object):
    def __init__(self):
        self.a, self.b = 0,1
    
    def __iter__(self): #声明迭代对象
        return self     #实例本身为迭代对象，故返回自己
    
    def __next__(self): #next 取值
        self.a, self.b = self.b, self.a + self.b #计算下一个值

        if self.a > 100000: #退出循环条件
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

# __getitem__ 可以用list方法按照下标取出元素或切片

class Fib0(object):
    def __getitem__(self, n):
        a, b = 1,1
        for x in range(n):
            a, b = b, a+b
        return a

f = Fib0()
print(f[0])
print(f[1])
print(f[10])
print(f[100])

# list还可以切片 但是在__getitem__中会报错
# 原因是__getitem__()传入的参数可能是一个int,也可能是一个切片对象 slice 因此需要进行判断

class Fib1(object):
    def __getitem__(self, n):
        if isinstance(n,int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a

        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop 
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L


ff = Fib1()
print(ff[0:5])
print(ff[:10])
# 另有__setitem__()方法，把对象视作list或者dict来对集合赋值
# __delitem__()方法用于删除某个元素

#__getattr__ 只有在未找到属性的情况下，才调用 __getattr__
class Student0(object):

    def __init__(self):
        self.name = 'Michael'
    
    def __getattr__(self,attr):     #调用未声明变量时调用此函数
        if attr=='score':
            return 99
        else:
            return 'nothing'        #此处也可返回函数



s0 = Student0()
print(s0.name)
print(s0.score)
print(s0.scsd)


# URL链式调用
class Chain(object):

    def __init__(self, path = ''):
        self._path = path
    
    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    
    __repr__ = __str__

print(Chain().status.user.timeline.list)

#调用对象实例的方法时，可以用instance.method()  直接在实例本身上调用方法要用__call__

class Student1(object):
    def __init__(self, name):
        self.name = name
    
    def __call__(self):
        print('My name is %s.' % self.name)

s1 = Student1('Michael')

s1()

#怎样判断一个变量是函数还是对象呢？
#能被调用的对象就是一个Callable对象

print(callable(Student0()))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))



    



    