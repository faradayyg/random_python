from multiprocessing import Pool
import time
import threading

COUNT = 50000000
def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=3)
    start = time.time()
    r1 = pool.apply_async(countdown, [COUNT//3])
    r2 = pool.apply_async(countdown, [COUNT//3])
    r3 = pool.apply_async(countdown, [COUNT//3])
    pool.close()
    pool.join()
    # thread = threading.Thread(target=countdown, args=(COUNT,))
    # thread.start()
    # thread.join()
    # countdown(COUNT)
    end = time.time()
    print('Time taken in seconds -', end - start)