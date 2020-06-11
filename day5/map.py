# map()
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6, 7, 8]
# def square(x):
#     return x ** 2
# map函数会把传入的list里面的每个值都进行square函数操作
# r = map(square, list_x)
r = map(lambda x, y: x * x + y, list_x, list_y)
print(list(r))
