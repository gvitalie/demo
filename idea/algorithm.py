import bisect
from random import randint, seed
import queue

kernel = 13
seed(kernel)

for _ in range(3):

    a = [randint(10, 99) for i in range(10)]
    print(a)

    q = queue.deque()

    while a:
        temp = a.pop()
        index = bisect.bisect_right(q, temp)
        q.insert(index, temp)
    print(q, '\n')
