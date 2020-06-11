# 装饰器
import time


# 对修改是封闭的，对扩展是开放的
def f1():
    # unix 时间戳
    # print(time.time())
    print('this is a function')


def f2():
    print('this is a function2')


def print_current_time(func):
    print(time.time())
    func()


print_current_time(f1)
print_current_time(f2)
