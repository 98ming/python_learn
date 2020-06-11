# filter
list_x = [1, 0, 1, 0, 1, 0]
list_u = ['a', 'B', 'c', 'D', 'e']
f = filter(lambda x: True if x != 0 else False, list_x)
u = filter(lambda x: True if x >= 'a' and x <= 'z' else False, list_u)
print(list(f))
print(list(u))
