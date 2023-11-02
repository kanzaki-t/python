"""
数据容器
    列表list
    元组tuple
    字符串str
    集合set
    字典dict

"""
# 定义列表
# > 变量名称 = [元素1，元素2，。。。]

# 定义空列表
# > 变量名称 = []
# > 变量名称 = list()

list_test = ["小明", "小红", "小蓝"]
str1 = list_test[0]
print(str1)

# list是一个类，list这个类中有很多方法

# 查找元素的下标 list名.index(元素)
print(list_test.index("小红"))

# 修改list中指定下标的值
list_test[2] = 55
print(list_test)  # ['小明', '小红', 55]

# 往list中指定下标的地方插入元素
list_test.insert(2, "被插入的元素")
print(list_test)  # ['小明', '小红', '被插入的元素', 55]

# 往list尾部追加1个元素
list_test.append("aaa")
print(list_test)  # ['小明', '小红', '被插入的元素', 55, 'aaa']

# 往list尾部追加一批元素
list_test.extend([1, 2, 3])
print(list_test)  # ['小明', '小红', '被插入的元素', 55, 'aaa', 1, 2, 3]

# 删除list的元素
# 1.del list[下标]
del list_test[1]
print(list_test)  # ['小明', '被插入的元素', 55, 'aaa', 1, 2, 3]

# 2.list.pop(下标) 有返回值
value = list_test.pop(2)
print(list_test)  # ['小明', '被插入的元素', 'aaa', 1, 2, 3]
print(value)  # 55

# 3.list.remove(元素) 删除某元素在列表中的第一个匹配项
mylist = [1, 9, 5, 9]
mylist.remove(9)
print(mylist)  # [1, 5, 9]

# 清空列表 list.clear()
mylist.clear()
print(mylist)  # []

# 统计某元素在列表内的数量 有返回值
mylist.extend([1, 3, 3, 8, 6, 1, 1, 8])
count = mylist.count(1)
print(count)  # 3

# 统计列表中所有元素的数量,即数组的长度
length = len(mylist)
print(length)  # 8
