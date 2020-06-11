# 列表推导式
# set、dict 也可以被推导
a = [1, 2, 3, 4, 5, 6, 7, 8]

# 普通列表推导式
b = [i * i for i in a]
print(b)  # [1, 4, 9, 16, 25, 36, 49, 64]
# 带条件筛选的列表推导式
b = [i * i for i in a if i >= 5]
print(b)  # [25, 36, 49, 64]

# dict 使用列表推导式
students = {
    '喜小磊': 18,
    '石敢当': 20,
    '横小五': 15
}
b = {value: key for key, value in students.items()}
print(b)    # {18: '喜小磊', 20: '石敢当', 15: '横小五'}
