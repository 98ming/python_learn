from people import People


# 子类继承父类
class Student(People):
    def __init__(self, school, name, age):
        self.school = school
        # People.__init__(self, name, age)
        super(Student, self).__init__(name, age)

    def do_homework(self):
        print('do homework')


student1 = Student('中北大学', '石敢当', 18)
# print(student1.__dict__)
# print(Student.sum)
print(student1.name)
print(student1.age)
print(student1.school)
# student1.get_name()
