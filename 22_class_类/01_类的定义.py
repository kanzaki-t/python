class Student:
    # 成员变量
    name = None
    age = None

    # 方法
    def say1(self, word):
        return word

    # 方法中需要访问类的成员变量，必须使用self,表示 类本身
    def say2(self):
        return f"你好，{self.name}"


stu1 = Student()
stu1.name = "小明"
stu1.age = 99
print(stu1.name)
print(stu1.age)
print(stu1.say1("aaa"))
print(stu1.say2())
