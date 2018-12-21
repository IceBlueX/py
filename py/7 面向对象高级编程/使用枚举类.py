from enum import Enum

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


#从Enum派生出自定义类
from enum import Enum, unique

@unique     #该装饰器可以检查有无重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)

print(Weekday.Tue)

print(Weekday['Tue'])
print(Weekday
.Tue.value)

print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)

print(Weekday(1))

print(day1 == Weekday(1))





