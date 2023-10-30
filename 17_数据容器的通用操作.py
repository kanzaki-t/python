list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)
str1 = "abcdefg"
set1 = {1, 2, 3, 4, 5}
dict1 = {
    "key1": 99,
    "key2": 66
}

# len() max() min()
print("len()")
print(len(list1))  # 5
print(len(tuple1))  # 5
print(len(str1))  # 7
print(len(set1))  # 5
print(len(dict1))  # 2

print("max()")
print(max(list1))  # 5
print(max(tuple1))  # 5
print(max(str1))  # g
print(max(set1))  # 5
print(max(dict1))  # key2 比较的是key

# 容器之间的转换
# list() tuple() str() set()
# 没有办法转换成字典 dict()

# 容器的排序
# sorted(容器，[reverse=True]) 得到的都是list
list1 = [5, 4, 3, 2, 1]
tuple1 = (5, 4, 3, 2,)
str1 = "gat"
set1 = {5, 4, 3, 2, }
dict1 = {
    "key1": 99,
    "key2": 66
}

print(sorted(list1))  # [1, 2, 3, 4, 5]
print(sorted(tuple1))  # [2, 3, 4, 5]
print(sorted(str1))  # ['a', 'g', 't']
print(sorted(set1))  # [2, 3, 4, 5]
print(sorted(dict1))  # ['key1', 'key2']
