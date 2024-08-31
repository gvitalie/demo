from random import randint, seed
from time import sleep

kernel = 13
seed(kernel)

tsec = 0.1
for i in range(3):
    try:

        match i:
            case 0:
                a = [i for i in range(10)]
            case 1:
                a = [i for i in range(9, -1, -1)]
            case 2:
                a = [randint(0, 100) for i in range(10)]


        print(a)
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
