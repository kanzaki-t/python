"""

"""
# 首先需要引入json模块
import json

data = [
    {
        "name": "jack",
        "age": 20
    },
    {
        "name": "roce",
        "age": 18
    }
]
print(type(data))  # <class 'list'>
# 把python数据转化成json数据
data1 = json.dumps(data)
print(data1)  # <class 'str'>
print(type(data1))

# 把json数据转化成python数据
data2 = json.loads(data1)
print(data2)
print(type(data2))  # <class 'list'>

# 以json形式写入文件
# data = [{"name": "jack", "age": 20}, {"name": "roce", "age": 18}]
data = {"name": "jack", "age": 20}
fw = open("json-w.txt", "w", encoding="UTF-8")
json.dump(data, fw)  # 方式一
# fw.write("\n")
# json.dump(obj=data, fp=fw)  # 方式二
# fw.write("\n")
# fw.write(json.dumps(data))  # 方式三
fw.close()

# 读取文件中的json数据
fr = open("json-w.txt", "r", encoding="UTF-8")
s = json.load(fr)
print("read")
print(s)
fw.close()
