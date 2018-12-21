from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    try:
        ss = exp.split('+')
        ns = map(str2num, ss)
    except IndentationError:
        print('Something Wrong')
    else:
        return reduce(lambda acc, x: acc + x, ns)
        raise
    finally:
        print('Finally>>>')

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)

    r = calc('99 + 88 + 8')       #修改7.6->8
    print('99 + 88 + 8 =', r)

main()
