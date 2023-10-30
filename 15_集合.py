"""
集合 set
    不支持元素的重复，而且无序

    变量名称 = {元素1，元素2，。。。元素}
    变量名称 = set{} # 定义一个空集合
"""

# 添加元素
set1 = {"a", 22}
set1.add("bbb")
print(set1)  # {'bbb', 'a', 22}

# 移除元素
set1.remove("a")
print(set1)  # {'bbb', 22}

# 取两个集合的差，并得到差的集合
# 集合1.difference(集合2)
# 集合1有 但是集合2没有的
set2 = {"aa", "bb", "cc"}
set3 = {"aa", "dd", "ee"}
set4 = set2.difference(set3)
print(set4)  # {'cc', 'bb'}

# 删除集合1中，和集合2相同的元素，所以集合1被修改，集合2不变
set2.difference_update(set3)
print(set2)  # {'bb', 'cc'}

# 合并两个集合
set4 = set2.union(set3)
print(set4)  # {'aa', 'bb', 'cc', 'ee', 'dd'}
