# 匿名函数
def add(x, y):
    return x + y


print(add(1, 2))

# 定义一个匿名函数
# lamdba parameter_list(参数列表): expression(表达式)
f = lambda x, y: x + y
print(f(1, 2))
# 三元表达式
# 条件为真时的返回结果 if 条件判断 else 条件为假时的返回结果
x = 2
y = 3
r = x if x > y else y
print(r)