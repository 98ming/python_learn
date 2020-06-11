# 模式
# 多个模式之间用 | 隔开
import re

qq = 'PythonC#\nJavaPHP'
r = re.findall('c#.{1}', qq, re.I | re.S)

print(r)
