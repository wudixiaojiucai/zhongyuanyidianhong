import pytest
from pythoncode.calculator import Calculator


class TestCalc:

    def setup_class(self):
        self.calc = Calculator()

    def setup_method(self):
        print("开始计算")

    def teardown_method(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,expect", [(3, 5, 8), (-1, -2, -3), (100, 300, 400)],
                             ids=["first add", "second add", "third add"]
                             )
    def test_calc_add(self, a, b, expect):
        """加法"""
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [(5, 2, 3), (4, -2, 6), (400, 300, 100)],
                             ids=["first sub", "second sub", "third sub"]
                             )
    def test_cale_sub(self, a, b, expect):
        """减法"""
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", [(5, 2, 10), (4, -2, -8), (400, 300, 120000)],
                             ids=["first mul", "second mul", "third mul"]
                             )
    def test_cale_mul(self, a, b, expect):
        """乘法"""
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [(6, 2, 3), (4, -2, -2), (400, 200, 2)],
                             ids=["first div", "second div", "third div"]
                             )
    def test_cale_div(self, a, b, expect):
        """除法"""
        assert expect == self.calc.div(a, b)
