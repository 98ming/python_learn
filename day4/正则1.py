import re

a = 'C|C++|Java|C#|Python|JavaScript'
# 利用python内置函数判断
res = a.index('Python')
print('Python' in a)
print(res)
# 利用正则判断
r = re.findall('Python', a)
if len(r) > 0:
    print('该字符串包含Python')
