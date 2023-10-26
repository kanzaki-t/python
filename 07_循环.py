"""
while 循环
    while 条件:
        ...
只要条件满足，就会无限循环
"""

num = 0
while num < 5:
    print("我想吃烤肉")
    num += 1


"""
for循环
    for 临时变量 in 待处理数据集:
    
临时变量，其作用域限定在循环内，
这种限定不是编程规范的限定，而非强制限定，即不会报错，
不遵守也可以正常运行，但是不推荐，
想要访问临时变量，可以预先在循环外定义变量
"""
name = "abcdefg"
for item in name:
    print(item)
