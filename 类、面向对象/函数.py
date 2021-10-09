############  函数 一  ############

import time

def test1():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('data.txt', 'a+', encoding='utf-8') as f:
        f.write('\n%s test1'%time_current)

test1()

############  函数二 传值方式 #################

# def test(*args): #把N个位置参数，以元组的类型打印
#     print(args)
# test(1,2,3,4,5,6)
#
# def test2(**kwargs): #把N个关键字参数，以字典的类型打印
#     print(kwargs)
# test2(name='qsj',age='25',sex='man')

###########  函数三 函数递归 ###############

def number(n):
    print(n)
    if int(n/2) > 0:
        return number(int(n/2))
    return n

number(10)

