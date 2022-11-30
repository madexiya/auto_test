import pytest

from pytest_live.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    def teardown_class(self):
        print("【结束测试】")

    def setup(self):
        print("【开始计算】")

    def teardown(self):
        print("【结束计算】")

    @pytest.mark.parametrize("a,b,result",
                             [(1, 1, 2),
                              (-0.01, 0.02, 0.01),
                              (10, 0.02, 10.02)
                              ], ids=["整数", "浮点型", "整形+浮点型"])
    @pytest.mark.p0
    def test_add1(self, a, b, result):
        assert self.calc.add(a, b) == result

    @pytest.mark.parametrize("a,b,result",
                             [(98.99, 99, 197.99),
                              (99, 98.99, 197.99),
                              (-98.99, -99, -197.99),
                              (-99, - 98.99, -197.99)])
    @pytest.mark.p1
    def test_add2(self, a, b, result):
        assert self.calc.add(a, b) == result

    @pytest.mark.parametrize("a,b,result",
                             [(99.01, 0, "参数大小超出范围"),
                              (-99.01, -1, "参数大小超出范围"),
                              (2, 99.01, "参数大小超出范围"),
                              (1, -99.01, "参数大小超出范围")])
    @pytest.mark.p1
    def test_add3(self, a, b, result):
        assert self.calc.add(a, b) == result

    @pytest.mark.parametrize("a,b,error_type",
                             [("文", 0, "TypeError"),
                              (4, "字", "TypeError")])
    @pytest.mark.p1
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
