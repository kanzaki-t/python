def user(name, age, gender):
    print(f"姓名是：{name}，年龄是：{age}，性别是：{gender}")


# 位置参数 -- 默认使用方式，严格按照顺序
user("tom", 20, "男")

# 关键字参数
user(name="jack", age=50, gender="man")
user(age=50, gender="man", name="jack")  # 可以不按照顺序
user("rose", age=50, gender="woman")  # 可以省略，但是按照顺序


# 缺省参数
def user(name, age, gender="男"):
    print(f"姓名是：{name}，年龄是：{age}，性别是：{gender}")


# 默认的性别是男，当不传参的时候，则使用默认参数
user("小明", 18)  # 姓名是：小明，年龄是：18，性别是：男
# 传参的情况下，则使用传参
user("小红", 22, "女")  # 姓名是：小红，年龄是：22，性别是：女


# 位置传递1
def user1(*args):
    """

    :param args: 传进的所有参数都会被args变量收集，不限数量
    :return: 并返回一个元组
    """
    print(args)


# 可以不传参
user1()  # 返回的是一个空元组（）

# ('小白', '小红', 88, [1, 2, 3], (9, 8, 7), ['list_ele1', 'list_ele2'], ('tuple_ele1', 'tuple_ele2'))
user1("小白", "小红", 88, [1, 2, 3], (9, 8, 7), ["list_ele1", "list_ele2"], ("tuple_ele1", "tuple_ele2"))


# 位置传递2
def user2(**kwargs):
    """

    :param kwargs: 参数是 键=值 形式的情况下会被kwargs接收，
    :return: 会返回字典
    """
    print(kwargs)


# 可以不传参
user2()  # 返回的是一个空字典{}

#
user2(name="孙悟空", age=9999)  # {'name': '孙悟空', 'age': 9999}
