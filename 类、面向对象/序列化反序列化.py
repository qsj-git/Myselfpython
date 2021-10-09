import json
'''
注意 json 只能处理简单的字符类型，像字符串，列表，字典等，
json 主要的作用是不同语言之间进行交互。
'''

data = {'k1': 1234, 'k2': 'hello'}

with open("data2.txt", 'w', encoding="utf-8") as file:
    file.write(json.dumps(data))      # json 序列化

with open("data2.txt", 'r') as fileb:
    print(json.loads(fileb.read()))   # json 反序列化

# import pickle
# with open("data2.txt",'wb') as file1:  # 要以二进制形式保存
#     file1.write(pickle.dumps(data))   # pickle 序列化会把内容用它自己的语法规则 以二进制的形式保存至文件
# with open("data2.txt",'rb') as file2:  # 以二进制形式读取
#     print(pickle.loads(file2.read())) # pickle 反序列化
