"""
字符串
    是字符的容器，和元组一样不可以修改
"""
name = "superman"

# 通过下标取值
value1 = name[1]
print(value1)  # u

# index取下标
print(name.index("r"))

# replace 替换
# 注意：不是修改字符串本身，而是得到了一个新的字符串
newname = name.replace("man", "woman")
print(name)  # superman
print(newname)  # superwoman

# split 按照字符串内的符号进行分割
list = name.split(",")
print(list)  # ['superman'] 由于没有“，”所以，没有分割
strs = "a b c d"
new_list = strs.split(" ")
print(new_list)  # ['a', 'b', 'c', 'd']

# strip() 去掉前后空格
# strip(字符串) 去掉前后的字符串
name3 = " aaaaa "
new_name3 = name3.strip()
print(new_name3)  # aaaaa

name4 = "1aaaaa2"
new_name4 = new_name3.strip("12")
print(new_name4)  # aaaaa
