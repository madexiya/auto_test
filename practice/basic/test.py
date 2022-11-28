# for i in range(10):
#     print(i)
#     if i == 3:
#         break
import random

# b = 1
# while b < 6:
#     print(b)
#     if b == 3:
#         b = b + 2.1
#         continue
#     b += 1

# 计算1-100求和
# 1.使用分支结构实现偶数求和
# sum = 0
# for i in range(1, 101):
#     if i % 2 != 0:
#         sum = sum + i
# print(sum)
# 2.不适用分支结构
# sum = 0
# for i in range(2, 101, 2):
#     sum = sum + i
# print(sum)

# 猜数字游戏
# 计算出一个1-100之间的随机数由人来猜，根据人猜的数字给出大一点、小一点、猜对了的提示
computer_num = random.randint(1, 100)
# print("computer_num:", computer_num)
while True:
    people_num = int(input("请输入你猜的数字："))
    if computer_num > people_num:
        print("大一点")
    elif computer_num < people_num:
        print("小一点")
    else:
        print("猜对了")
        break
