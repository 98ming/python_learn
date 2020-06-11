# match 和 search 函数
import re

qq = '8ABC3721D86'
# match会从字符串的开头尝试匹配，如果开头未匹配到则返回None
r = re.match('\d',qq)
# search 会搜索整个字符串，直到第一次匹配成功后立即返回匹配结果
s = re.search('\d',qq)
t = re.findall('\d',qq)
print(r.span())
print(s.group())
print(t)
