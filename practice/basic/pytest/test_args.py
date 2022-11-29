import pytest


# search_list = ['appium', 'selenium', 'pytest']
#
#
# @pytest.mark.parametrize('name', search_list)
# def test_search(name):
#     assert name in search_list

# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+5", 7), ("7+5", 12)],
#                          ids=["int1", "int2", "int3"])
# def test_mark_more(test_input, expected):
#     # eval 将字符串里的表达式计算出结果后返回
#     assert eval(test_input) == expected

@pytest.mark.parametrize("wd", ["appium", "selenium", "pytest"])
@pytest.mark.parametrize("code", [1, 2, 3])
def test_aaa(wd, code):
    print(f"wd:{wd},code:{code}")
