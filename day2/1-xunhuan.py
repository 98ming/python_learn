# while循环
condition = 1
while condition <= 10:
    print(condition)
    condition += 1
else:
    print('EOF')
# for循环
# 主要是用来遍历/循环 序列或者集合、字典
a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for x in a:
    for y in x:
        print(y)
else:
    print('fruit is gone')
for x in range(0, 10, 2):
    print(x, end=' | ')
