"""
lambda匿名函数
    语法：
        lambda 参数:函数体（只能写一行）
"""


def test(func):
    result = func(1, 2)
    print(result)


test(lambda x, y: x + y)
