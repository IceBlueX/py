
import numpy
import numpy as np




rate = 0
red_a = 0
blue_a = 0

j = 0
while j < 2000:
    red = 1  # 1
    blue = 1  # 0
    i = 0
    while i < 10000:

        next = np.random.binomial(1, float(red)/float(blue + red), 1)

        if int(next) == 1:
            red += 1
            red_a += 1
        else:
            blue += 1
            blue_a += 1

        i += 1
    print(red, blue)
    if red >= blue:
        rate += (float(red)/float(blue))
    else:
        rate += (float(blue) / float(red))

    j += 1

print(rate/2000)

print(red_a, blue_a, float(red_a)/float(blue_a))




