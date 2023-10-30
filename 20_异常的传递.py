def func1():
    print("func1开始执行了")
    num = 1 / 0
    print("func1结束执行了")


def func2():
    print("func2开始执行了")
    func1()
    print("func2结束执行了")


def main():
    try:
        func2()
    except Exception as e:
        print(f"出现的异常是：{e}")


# func1出现的异常，在main函数中获取
main()
