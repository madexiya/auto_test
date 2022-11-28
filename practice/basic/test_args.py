# def func1(*args):
#     print(args)
#
#
# func1("java", "python", "go")
# list1 = ["java", "python", "go"]
# func1(*list1)


def func2(**kwargs):
    print(kwargs)


# func2(name="tony", age=18)
dict1 = {"name": "jack", "age": 36}
func2(**dict1)


def greeting(name: str) -> str:
    name.strip()
    return 'hello' + name


greeting(" 123 ")

