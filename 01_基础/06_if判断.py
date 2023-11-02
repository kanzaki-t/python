"""
if 条件 :
elif 条件 ：
else ：
"""
age = input("请输入你的年龄")
age = int(age)
if 90 >= age > 18:
    print("可以吸烟啦")
elif age > 90:
    print("老不死的")
else:
    print("小p孩")