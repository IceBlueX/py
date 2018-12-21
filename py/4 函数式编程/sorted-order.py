#按照姓名和成绩进行排序
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

def by_name(s):
    return s[:1]
    
print(sorted(L,key=by_name))


def by_score(s):
    return s[-1:]

print(sorted(L,key=by_score,reverse=True))
