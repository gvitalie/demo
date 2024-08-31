To do: idea.

# Estimation

```Python
import math

p = 6
n = 10 ** p

sum_h = 0
for i in range(n + 1):
    h = (i * (n - i)) ** (1/2)
    sum_h += h

pi0 = 8 * sum_h / n / n

print(" ", math.pi)
print("~", pi0)

#   3.141592653589793
# ~ 3.141592650263593
```

# Incidence matrix

```Python
from random import randint, seed
from time import sleep

kernel = 13
seed(kernel)

tsec = 0.1
for i in range(3):
    try:
        a = [randint(0, 100) for i in range(10)]
        print(a)
        sleep(tsec)
        for i in range(len(a)):
            print("{:>4}:".format(a[i]), end=' ')
            index = 0
            for j in range(len(a)):
                state = int(a[i] > a[j])
                if state:
                    index += state
                print(state, flush=True, end=' ')
                sleep(tsec)
            print(f":{index}")
        print()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("\nStop")
        break

```

```Python
/home/me/PycharmProjects/demo/.venv/bin/python /home/me/PycharmProjects/demo/idea/incidence_matrix.py 
[33, 37, 87, 87, 23, 83, 29, 85, 18, 28]
  33: 0 0 0 0 1 0 1 0 1 1 :4
  37: 1 0 0 0 1 0 1 0 1 1 :5
  87: 1 1 0 0 1 1 1 1 1 1 :8
  87: 1 1 0 0 1 1 1 1 1 1 :8
  23: 0 0 0 0 0 0 0 0 1 0 :1
  83: 1 1 0 0 1 0 1 0 1 1 :6
  29: 0 0 0 0 1 0 0 0 1 1 :3
  85: 1 1 0 0 1 1 1 0 1 1 :7
  18: 0 0 0 0 0 0 0 0 0 0 :0
  28: 0 0 0 0 1 0 0 0 1 0 :2

[82, 93, 23, 16, 9, 68, 27, 95, 37, 3]
  82: 0 0 1 1 1 1 1 0 1 1 :7
  93: 1 0 1 1 1 1 1 0 1 1 :8
  23: 0 0 0 1 1 0 0 0 0 1 :3
  16: 0 0 0 0 1 0 0 0 0 1 :2
   9: 0 0 0 0 0 0 0 0 0 1 :1
  68: 0 0 1 1 1 0 1 0 1 1 :6
  27: 0 0 1 1 1 0 0 0 0 1 :4
  95: 1 1 1 1 1 1 1 0 1 1 :9
  37: 0 0 1 1 1 0 1 0 0 1 :5
   3: 0 0 0 0 0 0 0 0 0 0 :0

[55, 16, 87, 77, 1, 35, 18, 10, 33, 57]
  55: 0 1 0 0 1 1 1 1 1 0 :6
  16: 0 0 0 0 1 0 0 1 0 0 :2
  87: 1 1 0 1 1 1 1 1 1 1 :9
  77: 1 1 0 0 1 1 1 1 1 1 :8
   1: 0 0 0 0 0 0 0 0 0 0 :0
  35: 0 1 0 0 1 0 1 1 1 0 :5
  18: 0 1 0 0 1 0 0 1 0 0 :3
  10: 0 0 0 0 1 0 0 0 0 0 :1
  33: 0 1 0 0 1 0 1 1 0 0 :4
  57: 1 1 0 0 1 1 1 1 1 0 :7


Process finished with exit code 0
```

# Sorting algorithm using bisect

```Python
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
```

```Python
/home/me/PycharmProjects/demo/.venv/bin/python /home/me/PycharmProjects/demo/idea/algorithm.py 
[43, 47, 97, 97, 33, 93, 39, 95, 28, 38]
deque([28, 33, 38, 39, 43, 47, 93, 95, 97, 97]) 

[92, 33, 26, 19, 78, 37, 47, 13, 65, 26]
deque([13, 19, 26, 26, 33, 37, 47, 65, 78, 92]) 

[97, 87, 11, 45, 28, 20, 43, 67, 65, 27]
deque([11, 20, 27, 28, 43, 45, 65, 67, 87, 97]) 


Process finished with exit code 0
```
# Paradigm

```Python
me@amadeus:~$ python3 -q
>>> 
>>> import math
>>> 
>>> def exp(x):
...     a = 0
...     for i in range(100):
...             a = a + (x ** i) / math.factorial(i)
...     return a
... 
>>> def ln(x):
...     a = 0
...     for i in range(100):
...             a = a + 2 * (x - exp(a)) / (x + exp(a))
...     return a
... 
>>> def root(x, k):
...     a = 2
...     for i in range(100):
...             a = a - (a ** k - x) / (k * a ** (k - 1))
...     return a
... 
>>> 2 ** (1/2)
1.4142135623730951
>>> exp(1/2 * ln(2))
1.4142135623730956
>>> root(2, 2)
1.414213562373095
>>> 
>>> exp(1.23 * ln(3.21))
4.197601340269557
>>> exp(1/1.23 * ln(4.197601340269557))
3.2100000000000004
>>> ln(4.197601340269557)/ln(3.21)
1.23
>>> 
>>> # &•
>>> 
me@amadeus:~$ 
```