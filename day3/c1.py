"""
面向对象
有意义的面向对象的代码
类、对象
实例化
类最基本的作用：封装
"""


class Student():
    # 类变量
    name = '七月'

    # 构造函数,只能返回None
    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age

    def print_file(self):
        print('name: ' + self.name)
        print('age: ' + str(self.age))


# 实例化
student1 = Student('石敢当', 18)
print(student1.name)
print(Student.name)
