# 这个Animal就是抽象类，接口
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


dog: Dog = Dog()
cat: Cat = Cat()


def make_voice(animal: Animal):
    animal.speak()


make_voice(dog)
make_voice(cat)
