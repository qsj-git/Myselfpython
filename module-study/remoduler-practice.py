import re

s = '''bottle\nbag\nbig\napple'''

# 查看每个字符的下标
for i, c in enumerate(s, 1):
    print((i-1, c), end='\n' if i % 7 == 0 else '\t')
print()


# # ================================= 单次匹配 ================================
#
# match 方法,默认必须从0处匹配上，或指定位置开始匹配
m = re.match('b', s, re.M)
print(type(m), m)

regex = re.compile('^a', re.M)  # 提前编译正则，可以多次使用
m1 = regex.match(s, 14, 19)  # 从s这个字符串，下标14开始匹配，到19结束
m2 = regex.match(s, 15, 19)  # 从s这个字符串，下标14开始匹配，到19结束
print()
print(type(m1), m1)
print(type(m2), m2)

# search 方法,在字符串中搜索，从0或者指定位置开始向后搜索
m = re.search('^b', s)
print(type(m), m)

regex = re.compile('^bag', re.M)
m = regex.search(s, 7)
print(m)

# fullmatch 要求全长匹配，一个不落（如果指定子串，子串要全匹配）
fm = re.fullmatch('b.*', s, re.M | re.S)  # 用"^b"匹配不到，只能用'.*'
print(fm)

regex = re.compile('b.*', re.M)
fm = regex.fullmatch(s, 7, 10)
print(fm)


# ================================= 全文匹配 ================================

# findall 在文本中，全文搜索，匹配多次，返回列表，元素是字符串
fa = re.findall('b\\w+', s, re.M)
print(type(fa), fa)

regex = re.compile('b\\w+')
fa = regex.findall(s)
print(type(fa), fa)

for i in fa:    # 遍历查看匹配的结果，和类型
    print(type(i), i)

# finditer 全文搜索，但是返回迭代器，元素是Match对象
fi = re.finditer('b\\w+', s, re.M)
print(type(fi), fi)

for i in fi:
    print(type(i), i, i[0])  # 通过下标获取match值的方法，从python3.6开始可以使用
    # 以前获取match值的方法如下
    print(i.start(), i.end(), s[i.start():i.end()])


# ================================= 匹配替换 ================================

regex = re.compile('b\\wg')
result = regex.sub('111', s)  # 全文匹配，将匹配到的字符串替换成 111
print(1, type(result), result)

result = regex.sub('111', s, 1)  # 也可以指定次数，只匹配一次
print(2, type(result), result)
