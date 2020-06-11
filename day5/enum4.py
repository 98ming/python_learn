# 枚举
from enum import Enum


class VIP(Enum):
    YELLOW = 1
    # 相当于给YELLOW起了一个别称
    YELLOW_ALAIS = 1
    BLACK = 3
    RED = 4


# 普通遍历枚举类型，不带别称
for v in VIP:
    print(v)

# 特殊遍历枚举类型，带别称
for v in VIP.__members__:
    print(v)
