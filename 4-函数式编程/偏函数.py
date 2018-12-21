import functools

int2 = functools.partial(int,base=2)#偏函数
print(int2('1000000'))
print(int2('1010101'))

max2 = functools.partial(max,10)

print(max2(5,6,7))
print(max2(12,11,9))