# 添加线程
import threading
import time

def thread_job():
    print('T1 start')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish')

def main():
    added_thread = threading.Thread(target=thread_job)
    added_thread.start()
    # 加上 join 后主线程会等 add_thread 线程运行完后再执行主线程，同步的概念
    # 如果没有 join 就成异步
    added_thread.join()
    # 当前激活了几个线程 
    print(threading.active_count())
    # 当前运行的线程有哪些
    print(threading.enumerate())
    # 当前运行的线程
    print(threading.current_thread())


if __name__ == '__main__':
    main()