"""
字典 dict
    { key:value }
"""
dict1 = {
    "name": "jack",
    "age": 20
}

# 读取字典中指定key的值 dict[key]
print(dict1["name"])
print(dict1["age"])

# 更改元素
dict1["age"] = 99
print(dict1["age"])

# 新增元素
dict1["money"] = 10000
print(dict1["money"])
print(dict1)  # {'name': 'jack', 'age': 99, 'money': 10000}

# 删除元素
dict1.pop("money")
print(dict1)  # {'name': 'jack', 'age': 99}

# 获取全部的key
keys = dict1.keys()
print(keys)  # dict_keys(['name', 'age'])

# 循环
for key in keys:
    print(key)
    print(dict1[key])

for key in dict1:
    print(key)
    print(dict1[key])

# 取出key和value
print(dict1.items())  # dict_items([('name', 'jack'), ('age', 99)])
