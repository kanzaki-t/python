"""
导入模块
"""

# import 模块名
import time

print("aaa")
time.sleep(2)
print("bbbb")

# from 模块名 import 功能名 精确导入
from time import sleep

print("ccc")
sleep(2)
print("ddd")

# from time import * 通配符，代表模块种的所有内容
from time import *

print("eee")
sleep(2)
print("fff")

# import time as 别名 给模块起别名
# from time import sleep as 别名 给模块中的变量，函数起别名
import time as t

t.sleep(1)

from time import sleep as sl

sl(2)

# 自定义模块
"""
以_开头的变量
    在Python中，以下划线（underscore）开头的变量通常被用作内部变量或私有变量的约定。
    这意味着它们不应该在模块外部直接访问或修改。
__main__变量
    只想在模块中执行函数调用,则在模块中添加下述代码则可以实现
        if __name__ == '__main__'
            func()
__all__变量
    如果模块中没有定义__all__,则from time import *时，可以导出所有的变量和函数
    如果模块中定义了，如下：
    __all__ = ['func1']
        则from time import *时，只能调用func1
"""
