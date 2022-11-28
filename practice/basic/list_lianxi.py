# list_a = [1, 2, 3, 4, 5]
# list_a.pop(2)
# print(list_a)
#
# list_a.sort(reverse=True)
# print(list_a)
#
# list_b = ["python", "java", "go", "c"]
# list_b.sort(key=len)
# print(list_b)
#
# tup_a = (1, 2, 3, 3)
# print(tup_a)
#
# tup_b = (1, 2, 3, 4, 32, 55)
# print(tup_b[-1])
# # 元组解包
# tup_1 = 1, 2, 3
# a, b, c = (1, 2, 3)
# print(a, b, c)

# set_1 = {1, 2, 3}
# set_2 = {3, 4, 5}
# # print(set_1.union(set_2))
# # print(set_1 | set_2)
#
# print(set_1.difference(set_2))
# print(set_1 - set_2)
#
# dict1 = {"a": "123", "b": "456"}
# print(dict1["b"])
# dict1["b"]= 20
# print(dict1)
# dict1["c"] = 30
# print(dict1)
# 如果value值大于1，则将值进行平方运算并重新复制给key
# dict2 = {"a": 1, "b": 2, "c": 3}
# for k, v in dict2.items():
#     if v > 1:
#         dict2[k] = v ** 2
# print(dict2)
# 字典推导式
# dict3 = {"a": 1, "b": 2, "c": 3}
# dict4 = {k: v ** 2 for k, v in dict3.items() if v > 1}
# print(dict4)
# 给定一个字典对象，使用字典推导式，将它的key和value分别交换
# 输入{'a': 1,'b': 2,'c': 3}
# 输出{1:'a',2:'b',3:'c'}
dict5 = {'a': 1, 'b': 2, 'c': 3}
print(dict5.items())
dict6 = {v: k for k, v in dict5.items()}
print(dict6)
