"""
input 输入
print 输出
"""

print("请问你的名字叫做？")
name = input()
print(f"你好，{name}")

# 不用print()，直接在input的括号中输入内容也可以
# 输入的不管是什么，input返回的值都是字符串
age = input("你多大了？")
print(f"{age}岁？你看起来好年轻")

# print()不换行
print("aaa", end='')
print("bbb")