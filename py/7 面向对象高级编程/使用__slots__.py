# 给一个实例绑定方法

class Student(object):
    pass

s=Student()
s.name = 'Michael'  #动态给实例绑定一个属性
print(s.name)

def set_age(self,age):  # 定义一个函数作为实例方法
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age,s)   # 给实例绑定一个方法,但对其他实例不起作用
s.set_age(25) #调用实例方法
print(s.age)

def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)

s2 = Student() #创建新的实例
s2.set_score(99)
print(s2.score)

# 使用__slots__ 限制实例可添加的属性，仅对当前类实例起作用，对继承的子类不起作用
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99 //此处报错
#子类中也有__slots__,则子类可选范围为两者并集






