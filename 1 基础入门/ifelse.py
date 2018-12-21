h=float(input('height:'))
bim=80.5/(1.75**2)
if bim<18.5:
    print('过轻')
elif bim>=18.5 and bim<25:
    print('正常')
elif bim>=25 and bim<28:
    print('过重')
elif bim>=28 and bim<32:
    print('肥胖')
else:
    print('严重肥胖')

