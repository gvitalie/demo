from queue import Queue
import threading
from time import sleep
from random import randint


def producer(out_q):
    for i in range(10):
        tsec = randint(0, 3)
        message = f'{i} Hello. Wait: {tsec}'
        out_q.put(message)
        sleep(tsec)


def consumer(in_q):
    while True:
        message = in_q.get()
        in_q.task_done()
        print(message)


if __name__ == "__main__":
    q = Queue()
    producer_thread = threading.Thread(target=producer, args=(q,))
    producer_thread.daemon = True
    consumer_thread = threading.Thread(target=consumer, args=(q,))
    consumer_thread.daemon = True

    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
