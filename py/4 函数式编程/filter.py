#一解 reverse
def is_palindrome(s):
    k=[]
    while s!=0:
        k.append(s%10)
        s=int(s/10)
    m=list(k)
    k.reverse()
    return m==k

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')   

#二解 s[::-1]切片倒序
def is_pal(s):
    s=str(s)
    return s==s[::-1]
l=[x for x in range(1,1000)]
print(list(filter(is_pal,l)))

#三解 生成器一行计算100以内素数
print([x for x in range(1,101) if len(list(filter(lambda y:x%y==0,range(2,x))))==0])