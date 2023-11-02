"""
继承
    单继承
    class 类名(父类名)
"""


class Phone:
    IMEI = None  # 序列号
    producer = "Rf"  # 厂商

    def call_by_4g(self):
        print("4g")


class Phone2023(Phone):
    face_id = "1001"

    def call_by_5g(self):
        print("5g")


phone = Phone2023()
print(phone.IMEI)  # 可以读到父类Phone的IMEI
phone.call_by_4g()  # 可以读到父类Phone的call_by_4g方法

"""
继承
    多继承
    class 类名(父类名，父类名，...，父类名)
"""


class Phone1:
    IMEI = None  # 序列号
    producer = "Rf"  # 厂商

    def call_by_4g(self):
        print("4g")


class Camera:
    def take_photo(self):
        print("拍照")


class Phone2023_1(Phone1, Camera):
    pass  # 如果子类不需要额外的创建成员变量或方法，则可以使用关键字 pass


phone1 = Phone2023_1()
phone1.take_photo()  # 可以读到父类Camera的take_photo方法
phone1.call_by_4g()  # 可以读到父类Phone1的call_by_4g方法
