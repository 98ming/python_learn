# 字符集
import re

a = 'abc,acc,adc,aec,afc,ahc'
# 正则表达式两边的a和c是定界
# []里面的字符是或关系
# []里面的^表示取反操作
# [c-f]表示从c到f都是或关系，即[cdef]
r = re.findall('a[c-f]c', a)
print(r)
