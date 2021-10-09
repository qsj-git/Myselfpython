
# 面向对象(一)  实例变量与类变量

class Role(object):
    n = "这里是类变量"

    def __init__(self, name, role, gun, life_value=100):
        self.name = name
        self.roles = role
        self.gun = gun
        self.__life_value = life_value   # 私有属性

    def role(self):
        print("%s is a %s，剩余价值：%s " % (self.name, self.roles, self.__life_value))  # 私有属性只能在方法中调用

    def shot(self):
        print("%s is shotting " % self.name)

    def got_shot(self):
        print("%s is got shot……" % self.name)

    def buy_gun(self):
        print("%s bought %s" % (self.name, self.gun))


role1 = Role("qsj", "policeman", "AK47")
role1.role()
role1.shot()
role1.buy_gun()
print(role1.name)  # 调用公有属性正常
# print(role1.__life_value)  #调用私有属性报错

role2 = Role("wsx", "doctor", "M4A1")
print(role2.n)
print("---------"*3, "分割线", "---------"*3)
role2.n = "修改后的类变量"
print(role1.n)
print(role2.n)


''' # 面向对象(二) 类的继承

#class People():     # 经典类写法
class People(object): #新式类写法

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.firends = []

    def sleep(self):
        print("%s is sleeping……" % self.name)

    def number(self):
        print("%s is %s years old." % (self.name, self.age))


class Relation(object):
    def make_friends(self, obj):
        print("%s is making firends with %s " % (self.name, obj.name))
        self.firends.append(obj)


class Man(People):  #子类的继承
    def somking(self):
        print("%s is somking"% self.name)


class Women(People, Relation):   #多继承，继承了People和Relation两个父类
    def __init__(self, name, age, hair):  #重构，添加Women特有的特性
        #  People.__init__(self,name,age)  #经典类写法，重新继承父类
        super(Women, self).__init__(name, age) #新式类写法，重新继承父类
        self.hair = hair

    def shopping(self):
        print("%s like shopping." % self.name)

    def haircolor(self):
        print("%s hair is %s" % (self.name, self.hair))





man1 = Man("man","20")

# man1.sleep()
# man1.number()
# man1.somking()

women1 = Women("woman", "23", "yellow")
# women1.shopping()
# women1.haircolor()

women1.make_friends(man1)

print(women1.firends[0].name)
man1.name = "man2"
print(women1.firends[0].name)
'''
