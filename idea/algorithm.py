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
z = list()
n = 5
for k in range(1, 10 ** n, 10000):

    a = [randint(10, 99) for i in range(k)]
    x.append(k)
    print(k)
    # print(a)

    q = queue.deque()

    start = time.time()
    sorted(a)
    print(time.time() - start)
    z.append(time.time() - start)

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

plt.subplot(211)
plt.plot(x, y)
plt.plot(x, z)
plt.ylabel('Time (sec)')
plt.grid()

plt.subplot(212)
plt.plot(x, z)
plt.ylabel('Time (sec)')
plt.grid()

# plt.xscale('log')
plt.xlabel('Vector size')
plt.show()
