import re

a = 'C0C++7Java8C#9Python6JavaScript'
r = re.findall('\d', a)
# 'Python' 普通字符   '\d'  元字符
print(r)
