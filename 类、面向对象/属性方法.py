class Dog(object):
    name = "zxc"

    def __init__(self, name):
        self.name = name

    @property  #属性方法：把一个方法变成一个静态属性
    def eat(self):
        print("%s is eating dd " % self.name)

    @eat.setter
    def eat(self, food):
        print("set to food:", food)
        self.__food = food


d = Dog("wer")
d.eat
d.eat = "apple"
