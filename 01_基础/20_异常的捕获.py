"""
try:
    ...
except:
    ...
except 异常类型 as e:
    ...
"""

# 尝试打开一个不存在的文件,将会报错
try:
    f = open("abc.txt", "r", encoding="UTF-8")
except:
    print("捕获异常")

# 捕获指定类型的异常
try:
    print(age)
except NameError as e:
    print(e)  # name 'age' is not defined

# 捕获多个异常
try:
    # 1 / 0
    print(age)
except (NameError, ZeroDivisionError):
    print("出错了")

# 捕获所有异常
# 基础捕获异常的模式就可以捕获所有异常，除此之外还有以下方法
try:
    # 1 / 0
    # print(age)
    f = open("abc.txt", "r", encoding="UTF-8")
except Exception as e:
    print(e)

# else，finally
try:
    f = open("../json-w.txt", "r", encoding="UTF-8")
except Exception as e:
    print("出现异常了")
else:
    # 没有异常的情况下执行
    print("没有异常")
finally:
    # 有没有异常都会执行
    # 比如关闭文件
    f.close()
    print("有没有异常都会执行")
