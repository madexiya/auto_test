import logging

import allure
import pytest
import yaml


def get_datas(level):
    with open("datas.yaml", encoding="utf-8") as f:
        file_data = yaml.safe_load(f)
    add_datas = file_data.get("add").get(level).get("datas")
    add_ids = file_data.get("add").get(level).get("ids")
    return add_datas, add_ids


@allure.feature("计算器用例")
class TestCalc:
    @pytest.mark.parametrize("a,b,result", get_datas("p0")[0], ids=get_datas("p0")[1])
    @pytest.mark.p0
    @pytest.mark.run(order=3)
    @allure.story("p0有效边界值")
    def test_add1(self, a, b, result, get_calc):
        with allure.step("测试相加方法"):
            logging.info(f"参数{a},{b},期望结果：{result}")
        with allure.step("断言"):
            assert get_calc.add(a, b) == result

    @pytest.mark.parametrize("a,b,result", get_datas("p1_1")[0], ids=get_datas("p1_1")[1])
    @pytest.mark.p1_1
    @pytest.mark.run(order=1)
    @allure.story("p1_1有效边界值+无效边界值")
    def test_add2(self, a, b, result, get_calc):
        allure.attach.file("test_image.png", "测试图片", attachment_type=allure.attachment_type.PNG, extension=".png")
        assert get_calc.add(a, b) == result

    @pytest.mark.parametrize("a,b,error_type", get_datas("p1_2")[0], ids=get_datas("p1_2")[1])
    @pytest.mark.p1_2
    @pytest.mark.run(order=2)
    @allure.story("p1_2异常处理")
    def test_add3(self, a, b, error_type, get_calc):
        with allure.step("捕获异常"):
            with pytest.raises(eval(error_type)) as e:
                """error_type需要传入的是一个异常类型，传入字符串会报错，使用eval可以将字符串里的当做原始类型"""
                get_calc.add(a, b)
        with allure.step("打印异常名称"):
            print(e.typename)

    @pytest.mark.parametrize("a,b,error_type", get_datas("p2")[0], ids=get_datas("p2")[1])
    @pytest.mark.p2
    @pytest.mark.run(order=4)
    @allure.story("p2异常处理")
    def test_add4(self, a, b, error_type, get_calc):
        # 1、使用try except 捕获正常的异常TypeError
        # try:
        #     result = self.calc.add(a, b)
        # except TypeError as e:
        #     print(e)
        # 使用pytest封装的捕获正常的异常TypeError
        with pytest.raises(eval(error_type)) as e:
            """error_type需要传入的是一个异常类型，传入字符串会报错，使用eval可以将字符串里的当做原始类型"""
            get_calc.add(a, b)
        print(e.typename)
