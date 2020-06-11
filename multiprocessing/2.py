# queue 进程输出
import multiprocessing as mp


def job(q, a, b):
    res = 0
    for i in range(1000):
        res += i + i ** 2 + i ** 3
    q.put(res)  # queue


if __name__ == '__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q, 1, 2))
    p2 = mp.Process(target=job, args=(q, 1, 2))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1 + res2)
