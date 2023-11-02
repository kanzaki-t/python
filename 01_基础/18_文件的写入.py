# 打开文件
f = open("test1.txt", "w", encoding="UTF-8")

# 文件写入
f.write("hello worldaaaa")

# 文件刷新
# f.flush()

# 文件关闭 自带flush()功能
f.close()

# w的特点
# 当文件不存在时，则会创建新文件
# 如果文件存在，并且有内容的时候，则会把原有的内容清空之后写入新的内容
