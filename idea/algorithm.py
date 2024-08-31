import bisect
from random import randint, seed
import queue


if __name__ == "__main__":

    kernel = 13
    seed(kernel)

    for _ in range(3):

        a = [randint(10, 99) for i in range(10)]
        print(a)

        q = queue.deque()
        while a:
            bisect.insort(q, a.pop())
        print(q, '\n')
