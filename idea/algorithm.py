import bisect
from random import randint, seed
from time import sleep

kernel = 13
seed(kernel)

tsec = 1
for i in range(3):
    a = [randint(10, 99) for i in range(10)]
    print(a)
    for i in range(1, len(a)):
        temp = a.pop()
        index = bisect.bisect_right(a[:i], temp)
        a.insert(index, temp)
    print(a)
    print()
    sleep(tsec)
