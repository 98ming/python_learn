# 组
# 在需要重复匹配的普通字符加()，()里面的字符是且关系
import re

qq = 'PythonPythonPythonPythonPython'
r = re.findall('(Python){3}', qq)

print(r)
