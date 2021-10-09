'''生成器'''

'''
def fib(n):
    a, b, c = 0, 1, 0
    while c < n:
        yield (b)   #生成器就是，使用了yield的函数
        a, b = b, a+b
        c += 1

f=fib(5)
while True:
    try:
        print("number is :", f.__next__())
    except StopIteration :
        print("到底啦！")
        break
'''


#########  生成器的并行效果

import time


def func(name):
    print("生成器%s开始运行！" % name)
    while True:
        p = yield
        print("生成器%s几乎同时完成第%s次打印" % (name, p))


def func2():
    a = func("A")
    b = func("B")
    a.__next__()
    b.__next__()
    for i in range(10):
        time.sleep(1)
        a.send(i)
        b.send(i)


if __name__ == '__main__':
    func2()
