# 枚举小结
# IntEnum表示枚举值只能是int类型
# unique表示枚举值不能重复，即不允许有别称
from enum import IntEnum, unique

@unique
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

# 23种设计模式   枚举采用单例模式
# 枚举类型是不能实例化的
