from functools import reduce 

DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def str2float(l):
    def num(s):
        return DIGITS[s]
    n=0
    for x in l:  
        if x=='.':
            break
        n=n+1
    l1=reduce(lambda x,y:x*10+y,map(num,l[:n]))
    def fl(s):
        n=1
        m=0
        for x in s:
            m=m+x/(10**n)
            n=n+1
        return m
    l2=fl(list(map(num,l[n+1:])))
    return l1+l2

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
