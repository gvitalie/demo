from random import randint
from time import sleep

tsec = 0.1
while True:
    try:
        a = [randint(0, 100) for i in range(10)]
        print(a)
        sleep(tsec)
        for i in range(len(a)):
            print("{:>4}:".format(a[i]), end=' ')
            status = 0
            for j in range(len(a)):
                state = int(a[i] > a[j])
                if state:
                    status += state
                print(state, end=' ')
                sleep(tsec)
            print(f":{status}")
        print()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("\nStop")
        break
