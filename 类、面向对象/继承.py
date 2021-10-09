class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("%s is %s years old" % (self.name, self.age))


class Man(People):
    def __init__(self, name, age, money):
        super(Man, self).__init__(name, age)
        self.money = money

    def gender(self):
        print("%s is a Man,he is %s years old,he has ￥%s " % (self.name, self.age, self.money))


class Women(People):
    def shop(self):
        print("%s is a Women,she is %s years old,and she like shopping!" % (self.name, self.age))


Man1 = Man("qwe", 45, 100)
Man1.gender()

women1 = Women("lisa", 22)
women1.shop()
