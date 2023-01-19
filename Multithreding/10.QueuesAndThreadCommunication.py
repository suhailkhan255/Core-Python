import random
import time
import queue
from threading import *

def producer(q):
    while True:
        print('Producing')
        q.put(random.randint(1, 50))
        print("produced")
        time.sleep(3)

def consumer(q):
    while True:
        print("ready to consume")
        print('Consume Date: ', q.get())
        time.sleep(3)

q = queue.Queue()
t1 = Thread(target=consumer,  args=(q,))
t2 = Thread(target=producer,  args=(q,))

t1.start()
t2.start()

