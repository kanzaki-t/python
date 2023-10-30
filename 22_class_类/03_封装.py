"""
封装是把现实中的事物映射到类里的一种思想
"""

"""
私有化
    变量：变量名以双下划线开头
    方法：方法名以双下划线开头
    
    实际意义：
        在类中提供仅供内部使用的属性和方法，而不对外开放
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    __weight = 140

    def __getmoney(self):
        return "钱都给你"


stu1 = Student("小红", 18)
# print(stu1.__weight) 私有变量，类的对象访问不到
# stu1.__getmoney() 私有方法，类的对象访问不到
