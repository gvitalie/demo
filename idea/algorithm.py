import bisect
from random import randint, seed
from time import sleep
import queue

kernel = 13
seed(kernel)

tsec = 1
for i in range(3):

    a = [randint(10, 99) for i in range(10)]
    print(a)

    q = queue.deque()

    for i in range(1, len(a)+1):
        temp = a.pop()
        index = bisect.bisect_right(q, temp)
        q.insert(index, temp)
    print(q, '\n')
    sleep(tsec)
