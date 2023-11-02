"""
打开文件（创建文件）
    open(name,mode,encoding)
        - name:是要打开的目标文件名的字符串（可以包含文件所在的具体路径）
        - mode:设置打开文件的模式（访问模式）：只读"r"，写入"w"，追加"a"
        - encoding:编码格式（UTF-8）

    注意：encoding的顺序并不是第三位，所以不能用位置参数，必须用关键字参数直接指定
    ex.
        f = open("test.txt","r",encoding="UTF-8")
"""
# 打开（创建）文件
# f = open("test.txt", "r", encoding="UTF-8")

# 读取文件 read(num) num表示读取多少字节，如果不传入参数，则表示读取全部
# print(f.read(3))  # 你好，
# print(f.read())  # 你好，python！你好，java！

# 读取文件 readlines() 读取文件的全部行，封装到列表中
# lines = f.readlines()
# print(lines)  # ['你好，python！\n', '你好，java！']

# 读取文件 readline() 读取文件的一行
# print(f.readline())  # 你好，python！
# print(f.readline())  # 你好，java！

# 循环读取文件行
# for line in f:
#     print(line)
# 你好，python！
#
# 你好，java！

# 关闭文件
# f.close()

# with open() as f:
# 将会自动关闭文件(推荐)
with open("test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(line)
