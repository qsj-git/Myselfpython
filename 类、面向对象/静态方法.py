class Dog(object):
    def __init__(self, name):
        self.name = name

    @staticmethod  # 静态方法，名义上归类管理，实际上跟类没什么关系，在静态方法里访问不了类或实例中的如何属性
    def eat(self):
        print("%s is eating dd " % self.name)


d = Dog("wer")
d.eat(d)
