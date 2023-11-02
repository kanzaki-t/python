class Phone:
    IMEI = None  # 序列号
    producer = "父类producer"  # 厂商

    def call_by_4g(self):
        print("父类4g")


class Phone2023(Phone):
    producer = "子类producer"  # 复写父类的成员变量

    def call_by_4g(self):  # 复写父类的方法
        print("子类4g")
        # 调用父类的变量和方法
        # 方式一
        print(Phone.producer)  # 调用父类的变量
        Phone.call_by_4g(self)  # 调用父类的方法,需要用self参数
        # 方式二
        print(super().producer)  # 调用父类的变量
        super().call_by_4g()  # 调用父类的方法


phone = Phone2023()
print(phone.producer)  # 子类producer
phone.call_by_4g()  # 子类4g
