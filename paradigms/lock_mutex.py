"""
Concept being tested: Threading and Interpreter locks.

THREADING:
The average runtime of the program "single_thread" is 2 secs (because of the sleep)
the program below named single_thread is imitating an I/O bound task, hence multithreading
should speed up the pace at which multiple instances of single_thread is run by passing control to the thread not currently sleeping.
(Fair enough)

LOCKS:
with the introduction of locks, things take a different shape.
when a thread acquires a lock, nothing else can happen until said lock has been released
hence we are right back where we started. Right? Wrong.

You can acquire and release locks in strategic parts of your application making stuff "thread safe"
or avoiding race conditions.
"""

import threading
import concurrent.futures
from time import sleep, time


def single_thread(n):
    lock.acquire()
    print(f"Beginning of thread {n}")
    sleep(2)
    print(f"End of thread {n}")
    lock.release()


if __name__ == "__main__":
    start = time()
    print("Started main thread")
    lock = threading.Lock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        for i in range(2):
            ex.submit(single_thread, i)
    print("ended main thread")
    end = time()
    print(f"Ran for {end-start} seconds")
