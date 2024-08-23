import bisect
from random import randint, seed
from time import sleep
import queue
import time
import matplotlib.pyplot as plt

kernel = 13
seed(kernel)

tsec = 1

y = list()
x = list()
n = 5
for k in range(1, 10 ** n, 10000):

    a = [randint(10, 99) for i in range(k)]
    x.append(k)
    print(k)
    # print(a)

    q = queue.deque()

    start = time.time()
    for i in range(len(a)):
        temp = a.pop()
        index = bisect.bisect_right(q, temp)
        q.insert(index, temp)

    end = time.time()
    print(end-start)
    y.append(end-start)
    # print(q, '\n')
    sleep(tsec)


plt.plot(x, y)
# plt.xscale('log')
plt.xlabel('Vector size')
plt.ylabel('Time (sec)')
plt.grid()
plt.show()
