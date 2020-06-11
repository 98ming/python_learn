# 闭包 = 函数 + 环境变量
def curve_pre():
    a = 25

    def cureve(x):
        return a * x * x

    return cureve

a = 10
f = curve_pre()
print(f.__closure__)
# 查看闭包的环境变量
print(f.__closure__[0].cell_contents)
y = f(2)
print(y)
