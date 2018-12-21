it = iter([1,2,3,4,5])

while True:
    try:
        print(next(it))
    except StopIteration:
        break