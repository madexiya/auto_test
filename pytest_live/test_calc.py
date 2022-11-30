import pytest
import yaml

from pytest_live.calculator import Calculator


def get_datas(level):
    with open("datas.yaml", encoding="utf-8") as f:
        file_data = yaml.safe_load(f)
    add_datas = file_data.get("add").get(level).get("datas")
    add_ids = file_data.get("add").get(level).get("ids")
    return add_datas, add_ids


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    def teardown_class(self):
        print("【结束测试】")

    def setup(self):
        print("【开始计算】")

    def teardown(self):
        print("【结束计算】")

    @pytest.mark.parametrize("a,b,result", get_datas("p0")[0], ids=get_datas("p0")[1])
    @pytest.mark.p0
    @pytest.mark.run(order=3)
    # p0有效边界值
    def test_add1(self, a, b, result):
        assert self.calc.add(a, b) == result

    @pytest.mark.parametrize("a,b,result", get_datas("p1_1")[0], ids=get_datas("p1_1")[1])
    @pytest.mark.p1_1
    @pytest.mark.run(order=1)
    def test_add2(self, a, b, result):
        assert self.calc.add(a, b) == result

    @pytest.mark.parametrize("a,b,error_type", get_datas("p1_2")[0], ids=get_datas("p1_2")[1])
    @pytest.mark.p1_2
    @pytest.mark.run(order=2)
    # 异常处理
    def test_add3(self, a, b, error_type):
        with pytest.raises(eval(error_type)) as e:
            """error_type需要传入的是一个异常类型，传入字符串会报错，使用eval可以将字符串里的当做原始类型"""
            self.calc.add(a, b)
        print(e.typename)

    @pytest.mark.parametrize("a,b,error_type", get_datas("p2")[0], ids=get_datas("p2")[1])
    @pytest.mark.p2
    @pytest.mark.run(order=4)
    # 异常处理
    def test_add4(self, a, b, error_type):
        # 1、使用try except 捕获正常的异常TypeError
        # try:
        #     result = self.calc.add(a, b)
        # except TypeError as e:
        #     print(e)
        # 使用pytest封装的捕获正常的异常TypeError
        with pytest.raises(eval(error_type)) as e:
            """error_type需要传入的是一个异常类型，传入字符串会报错，使用eval可以将字符串里的当做原始类型"""
            self.calc.add(a, b)
        print(e.typename)
