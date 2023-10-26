
flag = True

while flag:

    try:
        total_time = int(input("请输入剩余时长"))
        num = total_time/4/60
        num = round(num)
        print("每个需要%d根" % num)
        flag = False
    except ValueError:
        input("请输入数字")

