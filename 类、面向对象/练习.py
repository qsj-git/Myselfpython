'''    练习1--拷贝文件   '''
'''
def copy(src_fname,dst_fname) :
    with open(src_fname, 'r', encoding='utf-8') as srcf, \
            open(dst_fname, 'w', encoding='utf-8') as dstf:
        while True:
            data = srcf.read(4096)
            if not data:
                break
            dstf.write(data)

copy('data.txt','databak')
'''


'''  练习2--每个以py结尾的文件，都是一个模块，如果在同一目录下，可以直接调用'''
# import cmodule
# print(cmodule.hi)
# cmodule.pstar(20)



'''  练习3
1、设置一个用于随机取出字符的基础字符串，本例使用大小写字母加数字
2、循环n次，每次随机取出一个字符
3、将各个字符拼接起来，保存到变量result中
'''

from random import choice
import string

all_chs = string.ascii_letters + string.digits  #大小写字母加数字
def gen_pass(n=8):
    result = ''

    for i in range(n):
        ch = choice(all_chs)
        result += ch
    return result

# if __name__ == '__main__':
#     print(gen_pass())
#     print(gen_pass(10))


'''进阶练习--编写登陆接口
1.输入用户名密码
2.如果没有该用户则提示创建，并随机生成密码，并且保存至文件
3.认证成功后显示欢迎信息
4.输错三次后锁定
'''

import cmodule
choices = input("新建账号，还是用已有账号登陆(N/Y)：")

if choices.upper() == "N":
    cmodule.newly()
elif choices.upper() == "Y":
    cmodule.login()
else:
    quit()

