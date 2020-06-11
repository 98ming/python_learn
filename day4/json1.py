import json

json_str = '[{"name":"七月","age":18,"flag":false},{"name":"七月","age":18}]'
# 反序列化
student = json.loads(json_str)

print(type(student))
print(student)
# print(student['name'])
# print(student['age'])
