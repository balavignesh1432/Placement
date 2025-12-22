from threading import Semaphore, Thread, Lock
from collections import deque

filled = Semaphore(0)
empty = Semaphore(10)
mutex = Semaphore(1)    # Binary Semaphore
# mutex = Lock()          # Or mutex (Ownership)
buffer = deque()
# Producer
def producer():
    count = 0                                    # Some data, Local to thread not shared
    while True:
        empty.acquire()
        mutex.acquire()
        print("Producing", count)
        buffer.append(count)                     # Add to buffer
        count += 1
        mutex.release()
        filled.release()

# Consumer
def consumer():
    while True:
        filled.acquire()
        mutex.acquire()
        print("consuming", buffer.popleft())   # FIFO Consumption
        mutex.release()
        empty.release()

producerThreads = [Thread(target=producer) for _ in range(3)]
consumerThreads = [Thread(target=consumer) for _ in range(3)]

for t, c in zip(producerThreads, consumerThreads):
    t.start()
    c.start()

# Do some other task, threads run in background

for t, c in zip(producerThreads, consumerThreads):
    t.join()
    c.join()

# Only after all thread complete this section 