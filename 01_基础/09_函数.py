"""
函数
    def 函数名(参数):
        函数体
        return 返回值
"""


# 附带函数的文档说明
def add(m, n):
    """
    加法运算
    :param m: 任意数字
    :param n: 任意数字
    :return: 数字相加的和
    """
    res = m + n
    return res


x = add(2, 4)
print(x)

# 函数内修改全局变量
num = 100


def func_a():
    global num
    num = 500


func_a()
print(num)  # 500
