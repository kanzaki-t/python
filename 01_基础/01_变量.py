# 格式：变量名 = 变量值
name = "小明"
print(name)
print(type(name))  # <class 'str'>

# 没有对变量进行类型固定化
name = 10
print("被赋值数字之后name为：", name)

print(type(name))  # <class 'int'>

# 可以给多个变量赋值
x = y = z = 18
a, b, c = 11, 22, 33
