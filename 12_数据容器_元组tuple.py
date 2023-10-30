"""
元组 tuple
    重点：元组一旦创建之后，则不可以再被修改
         但是如果元组里面的元素是list，list的元素则可以被修改

    变量名称 = (元素1，元素2，。。。元素)
    变量名称 = tuple(元素1，元素2，。。。元素)

    同样可以用 while 和 for 遍历
"""
# 单个元素的元组,必须加逗号
t1 = ("aaa",)
print(type(t1), t1)  # <class 'tuple'> ('aaa',)

# 通过下标查找元素
t2 = ("aaaa", 123)
print(t2[0])  # "aaaa"
print(t2[1])  # 123

# 查找元素的下标
print(t2.index(123))  # 1

# 查找元素出现的次数
t3 = (1, 1, 3)
print(t3.count(1))  # 2

# 元组的长度
print(len(t3))  # 3

# 遍历
for x in t3:
    print(x)
