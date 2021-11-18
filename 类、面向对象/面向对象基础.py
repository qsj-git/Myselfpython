class Person:  # 解释器会为我们创建全局变量Person指向类对象

    def __init__(self):
        print(1, id(self))

    def showid(self):
        print(2, id(self))


tom = Person()
print(id(tom))
tom.showid()
print()
jerre = Person()
print(id(jerre))
jerre.showid()
