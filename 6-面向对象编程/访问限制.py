#变量前加双下划线__表示该变量为私有变量 private
#变量前后均有双下划线，是特殊变量，特殊变量是可以直接访问的
#变量前有单下划线，表示该变量虽然可以任意访问，但不要随意访问
#即使变量前有双下划线，也可以通过类名加变量名来访问 如，_Student__name
class Student(object):

    def __init__(self, name, score,gender):
        self.__name = name
        self.__score = score
        self.__gender = gender

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_gender(self):
        return self.__gender


    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score') 

    def set_gender(self,gender):
        if gender=='male':
            self.__gender = gender
        elif gender=='female':
            self.__gender =gender
        else:
            raise ValueError('bad gender')      


#bart = Student('Bart Simpson', 59)

#print_score(bart)

bart = Student('Bart', 35,'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
