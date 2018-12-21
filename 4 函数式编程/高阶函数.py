def add(a,b,f):
    return f(a)+f(b)

print(add(-2,4,abs))
print(add(-6,-7,abs))
