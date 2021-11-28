class Person():
    def __init__(self, name, sex, age=18):
        self.__name = name
        self.__age = age
        self._sex = sex  # protected 保护的成员：_<name>  在python中没有实现，社区定义的，等效于public。

    # private 私有member成员：__<name>，包括类属性，实例属性，私有的。仅限于在类中调用。_当前类 作为前缀。当前类中使用
    def __showme(self):
        print("{} is {} years old ,he is a {} !".format(self.__name, self.__age, self._sex))

    # public 公有成员： 类里面、外面都能调用
    def showme(self):
        return self.__showme()


if __name__ == '__main__':
    tom = Person('T', 'man')
    print(tom.__dict__)
    print(tom._sex)
    #tom.__showme() 私有成员，无法在实例中被调用
    tom.showme()
