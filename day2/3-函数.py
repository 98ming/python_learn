def add(x, y):
    return x + y


def my_print(x):
    print(x)


def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 6
    return damage1, damage2


# a = add(1, 2)
# b = my_print('python')
# print(a, b)
skill_damage1, skill_damage2 = damage(1, 3)
print(skill_damage1, skill_damage2)
print(damage(1, 3))
