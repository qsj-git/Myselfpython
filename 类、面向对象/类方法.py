class Dog(object):
    name = "zxc"

    def __init__(self, name):
        self.name = name

    @classmethod  #类方法只能访问类变量，不能访问实例变量
    def eat(self):
        print("%s is eating dd " % self.name)


d = Dog("wer")
d.eat()
