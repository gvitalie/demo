To do: idea.

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
```

```Python
/home/me/PycharmProjects/demo/.venv/bin/python /home/me/PycharmProjects/demo/idea/algorithm.py 
[43, 47, 97, 97, 33, 93, 39, 95, 28, 38]
[28, 33, 38, 39, 43, 47, 93, 95, 97, 97]

[92, 33, 26, 19, 78, 37, 47, 13, 65, 26]
[13, 19, 26, 26, 33, 37, 47, 65, 78, 92]

[97, 87, 11, 45, 28, 20, 43, 67, 65, 27]
[11, 20, 27, 28, 43, 45, 65, 67, 87, 97]


Process finished with exit code 0
```