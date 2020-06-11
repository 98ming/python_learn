# 闭包解决旅行者行走问题

origin = 0


def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos

    return go


f = factory(origin)
print(f(2))
print(f(3))
print(f(6))
