# 概括字符集
#   \w相当于[A-Za-z0-9_] \w被叫做概括字符集
import re
# \d \D
# \w 单词字符 \W
# \s 空白字符 \S
a = 'python 1\t111&java_\r678\nphp'
r = re.findall('\s', a)
print(r)

