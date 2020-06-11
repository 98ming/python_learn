class Student:
    # 类变量
    name = '七月'
    sum = 0

    # 构造函数,只能返回None
    def __init__(self, name1, age):
        # 实例变量
        self.name = name1
        self.age = age
        self.__score = 0

    # 实例方法
    def print_file(self):
        print('name: ' + self.name)
        print('age: ' + str(self.age))

    # 在函数名或者变量前面加双下划线，此函数或变量就变成了一个私有函数或变量
    # 注意：千万不要画蛇添足，在私有函数或私有变量的函数名或者变量名后面在添加双下划线
    def marking(self, score):
        if score < 0:
            return '不能给人打负分'
        else:
            self.__score = score
            print(self.name + '同学的成绩为：' + str(self.__score))

    # 类方法
    @classmethod
    def student_sum(cls):
        # 访问类变量
        cls.sum += 1
        print('当前班级学生总数为：' + str(cls.sum))

    # 静态方法
    @staticmethod
    def add(x, y):
        print(Student.sum)


# 实例化
student1 = Student('石敢当', 18)
result = student1.marking(20)
student1.__score = -1
print(student1.__score)
print(student1.__dict__)
