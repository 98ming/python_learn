# 装饰器
import time


def decorator(func):
    # *args 表示多个参数，从而解决调用多个参数的函数时传入的参数不足的问题
    # **kw 表示多个关键字参数
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)

    return wrapper


# 装饰器名称
@decorator
# 不改变原来函数的调用方法,从而添加新的功能
def f1(func_name):
    print('this is a function ' + func_name)


@decorator
def f2(x, y):
    print(x + y)


@decorator
def f3(x, y, **kw):
    print(x + y)
    print(kw)


f1('test func')
f2(1, 2)
f3(1, 2, a='1', b='2')
# f = decorator(f1)
# f()
