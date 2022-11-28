import json

# data = {
#     'a': 1,
#     'b': ['2', '3'],
#     'c': True,
#     'd': False,
#     'e': None
# }
# Python对象转换为json
# json_data = json.dumps(data)
# print(json_data)

# json数据转换为Python对象
# json_data = '''{"a": 1, "b": ["2", "3"], "c": true, "d": false, "e": null}'''
# python_data = json.loads(json_data)
# print(python_data)

# 把python对象转换为json，并写入json文件
# data2 = {
#     'a': 1,
#     'b': ['2', '3'],
#     'c': True,
#     'd': False,
#     'e': None
# }
# with open("data.json", "w") as f:
#     json.dump(data2, f)

# 读取json文件，并转换为Python对象
# with open("data.json", "r") as f:
#     python_data2 = json.load(f)
# print(python_data2)

data3 = {
    'a': 1,
    'b': "测试开发",
    'c': True,
    'd': False,
    'e': None
}
# python对象中包含中文时，ensure_ascii设置为False才不会乱码，indent为设置缩进
json_data3 = json.dumps(data3, ensure_ascii=False, indent=3)
print(json_data3)
