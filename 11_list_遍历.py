"""
while 遍历
"""
print("while 遍历")
mylist = [1, 2, 3, 4, 5]
index = 0
while index < len(mylist):
    ele = mylist[index]
    print(ele)
    index += 1
"""
for 遍历（推荐：写法简单）
"""
print("for 遍历")
for x in mylist:
    print(x)
