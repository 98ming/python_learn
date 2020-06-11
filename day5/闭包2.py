def f1():
    a = 10

    def f2():
        # a此时被python认为是一个局部变量
        # 如果依然对a进行赋值，此时将不会看成一个闭包
        # a = 20
        c = 20 * a
        print(a)
    return f2

f = f1()
print(f)
print(f.__closure__)
