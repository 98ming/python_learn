# 效率对比 multiprocessing multithreading
import multiprocessing as mp
import threading as td
import time


def job(q):
    res = 0
    for i in range(100000):
        res += i + i ** 2 + i ** 3
    q.put(res)  # queue


def multi_process():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multiprocess:', res1 + res2)


def multi_thread():
    q = mp.Queue()
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)


def normal():
    res = 0
    for j in range(2):
        for i in range(1000000):
            res += i + i ** 2 + i ** 3
    print('normal:', res)


if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time:', st1 - st)
    st2 = time.time()
    multi_thread()
    print('multithread time:', time.time() - st2)
    st3 = time.time()
    multi_process()
    print('multiprocess time:', time.time() - st3)
