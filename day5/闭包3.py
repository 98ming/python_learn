# 非闭包解决旅行者行走问题
origin = 0

def go(step):
    global origin
    new_step = origin + step
    origin = new_step
    return origin

print(go(2))
print(go(3))
print(go(6))