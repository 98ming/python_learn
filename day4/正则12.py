import re

qq = 'life is short,i use python,i love python'
r = re.findall('life(.*)python(.*)python', qq)
print(r)
