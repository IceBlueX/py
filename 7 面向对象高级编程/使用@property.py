'''class Student(object):

    def get_score(self):
        return self._score
    
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        
        if value<0 or value > 100:
            raise ValueError('score must between 0~100 !')
        self._score = value

s = Student()
s.set_score(60)
print(s.get_score())

#s.set_score(9999)   此处报错 '''

#内置的@property装饰器：把一个方法变成属性调用

#既能检查参数，又可以用类似属性的方式来访问类变量

'''
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value<0 or value>100:
            raise ValueError('score must between 0 ~ 100!')
    
        self._score = value

s = Student()
s.score = 80
#s._score = 60
print(s._score)

#s.score = 9999 #此处报错   '''

#定义只读属性，只定义getter方法，不定义setter方法

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):                  # 只读属性，age根据birth和当前时间计算出来
        return 2018 - self._birth

s = Student()
s.birth = 1994
print(s._birth)
print(s.age) #'''

    

    





