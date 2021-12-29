class Dog(object):

    def __init__(self, food):
        self.__food = food

    @property  #属性方法：把一个方法变成一个静态属性
    def eat(self):    # getter 名
        print("he is eating %s " % self.__food)

    @eat.setter      # 这边的eat是getter名，要与getter名字保持一致
    def eat(self, food):   # setter 名，要与getter名字保持一致
        print("set to food:", food)
        self.__food = food


d = Dog("wer")
d.eat
d.eat = "apple"
# d.eat