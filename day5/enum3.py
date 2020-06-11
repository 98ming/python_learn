# 枚举
from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


res = VIP.YELLOW == VIP.RED
# 枚举变量之间是不能做大小比较的，但可以做等值比较
# res2 = VIP.YELLOW > VIP.RED
res1 = VIP.YELLOW != VIP.BLACK
res2 = VIP.YELLOW is VIP.BLACK
print(res)
print(res1)
print(res2)
