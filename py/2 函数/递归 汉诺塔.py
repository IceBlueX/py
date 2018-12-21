def move(n,a='A',b='B',c='C'):
    if n==1:
        return print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(32)
        