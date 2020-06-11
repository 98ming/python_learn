day = 2


def get_sunday():
    return 'Sunday'


def get_monday():
    return 'Monday'


def get_tuesday():
    return 'Tuesday'


def get_default():
    return 'None'


switcher = {
    0: get_sunday,
    1: get_monday,
    2: get_tuesday
}
# day_name = switcher[day]
# 字典的第二种取值方法,get函数，第二个参数是如果没有key值的话
day_name = switcher.get(day, get_default)()
print(day_name)
