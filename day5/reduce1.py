# reduce函数
# reduce的第三个参数是进行计算的初始值
from functools import reduce

list_x = [1, 2, 3, 4, 5, 6, 7, 8]
# 连续计算，连续调用lambda
# 会把lambda表达式的计算结果当做下一次lambda的参数进行计算
# ((((1+2))+3)+4)+5......
r = reduce(lambda x, y: x + y, list_x, 10)

print(r)
