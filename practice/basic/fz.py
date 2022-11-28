# class Human:
#     def live(self):
#         print(f"住在地球上")
#
#
# class Student(Human):
#     def live(self):
#         print("住在学校里")
#
#
# stu = Student()
# stu.live()

with open("./data.txt", "a+", encoding="utf-8") as f:
    f.write("test_sb!!!")
    print(f.read())
    f.close()
