from threading import Semaphore, Lock, Thread

mutex = Lock()
countSem = Semaphore(1)
turnStile = Semaphore(1)
threadCount = 0
def reader1():
    global threadCount          # Important: to indicate use global variable
    while True:
        countSem.acquire()
        threadCount += 1
        if threadCount == 1:
            mutex.acquire()
        countSem.release()

        print("Reading")
        
        countSem.acquire()
        threadCount -= 1
        if threadCount == 0:
            mutex.release()
        countSem.release()

def reader2():
    global threadCount          # Important: to indicate use global variable
    while True:
        turnStile.acquire()
        countSem.acquire()
        turnStile.release()
        threadCount += 1
        if threadCount == 1:
            mutex.acquire()
        countSem.release()

        print("Reading")
        
        countSem.acquire()
        threadCount -= 1
        if threadCount == 0:
            mutex.release()
        countSem.release()


def writer():
    while True:
        turnStile.acquire()
        mutex.acquire()
        turnStile.release()
        print("Writing")
        mutex.release()

readerThreads = [Thread(target=reader2) for _ in range(3)]
writerThreads = [Thread(target=writer) for _ in range(3)]

for r, w in zip(readerThreads, writerThreads):
    r.start()
    w.start()

# Do Something

for r, w in zip(readerThreads, writerThreads):
    r.join()
    w.join()
