# 打开文件
f = open("test1.txt", "a", encoding="UTF-8")

# 文件写入
f.write("\nadd")

# 文件关闭 自带flush()功能
f.close()
