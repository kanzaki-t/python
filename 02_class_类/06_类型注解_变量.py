# 基础数据类型注解
# 方式一
var1: int = 10
var2: str = "hello"
var3: bool = True
# 方式二
var4 = 10  # type: int
var5 = "hello"  # type: str
var6 = True  # type: bool


# 类对象的类型注解
class Student:
    pass


stu: Student = Student()

# 基础容器类型注解
list1: list = [1, 2]
tuple1: tuple = (1, 2, 3)
dict1: dict = {"age": 20}

# 容器类型详细注解
list2: list[int] = [1, 2]
tuple2: tuple[int, str, bool] = (1, "a", False)
dict2: dict[str, int] = {"age": 20}
