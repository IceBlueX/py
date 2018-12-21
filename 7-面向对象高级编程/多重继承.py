# 多重继承 MixIn

class Animal(object):
    pass

#大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixin(Animal):
    def run(self):
        print('Running...')

class FlyableMixin(Animal):
    def fly(self):
        print('Flying...')

class CarnivorousMixin(Animal):
    def eatmeat(self):
        print('Eat Meat')

class HerbivoresMixin(Animal):
    def eatgrass(self):
        print('Eat Grass')


#各种动物
class Dog(Mammal,Runnable):
    pass

class Bat(Mammal,Flyable):
    pass

class Parrot(Bird,Flyable):
    pass

class Ostrich(Bird,Runnable):
    pass


#python 自带TCPServer和UDPServer 同时服务多个用户就必须使用多进程或多线程
#多进程模型 ForkingMixIn
#多线程模型 ThreadingMixIn

#多线程TCP
class MyTCPServer(TCPServer, ForkingMixIn):
    pass

#多线程UDP
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass

