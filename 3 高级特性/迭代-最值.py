def findMinAndMax(L):
    if L[:1]:
        max=L[0]
        min=L[0]
        for num in L:
            if num>max:
                max=num
            if num<min:
                min=num
        return (min,max)
    else:
        return (None,None)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')