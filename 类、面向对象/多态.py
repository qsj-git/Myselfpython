class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

    @staticmethod
    def animal_talk(obj):
        obj.talk()


class Dog(Animal):
    def talk(self):
        print("汪！")


class Cat(Animal):
    def talk(self):
        print("喵！")


c = Cat("cat1")

d = Dog("dog1")

Animal.animal_talk(c)
Animal.animal_talk(d)
