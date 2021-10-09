'''装饰器'''

import time

def timer(func):   # 装饰器
    def deco(*args,**kwargs):    # 嵌套函数
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print("The func is run time %s:"%(stop_time-start_time))
    return deco    #高阶函数,返回deco函数内存地址

@timer    #调用装饰器,test1=timer(test1)
def test1():
    time.sleep(2)
    print("this is test1")

test1()

@timer
def test2(name,age):
    print("he name is %s,%s years old!"%(name,age))

test2("qwe",22)