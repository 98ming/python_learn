# 枚举
from enum import Enum


# 枚举和普通类相比有什么优势
# 枚举变量不可更改
# 枚举可以方正出现重复标签
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

print(type(VIP.YELLOW))
# print(type(VIP['YELLOW']))
print(VIP.YELLOW.name)
print(VIP.YELLOW.value)
