import pytest
from test_pytest_work.read_yaml import read_yaml


class TestCalc:
    add_data = read_yaml("./case_data.yaml")["add_data"]
    sub_data = read_yaml("./case_data.yaml")["sub_data"]
    mul_data = read_yaml("./case_data.yaml")["mul_data"]
    div_data = read_yaml("./case_data.yaml")["div_data"]
    case_name = read_yaml("./case_data.yaml")["ids"]

    @pytest.mark.parametrize("a,b,expect", add_data, ids=case_name)
    def test_calc_add(self, auto_fixture, a, b, expect):
        """加法"""
        calc = auto_fixture
        assert calc.add(a, b) == expect

    @pytest.mark.parametrize("a,b,expect", sub_data, ids=case_name)
    def test_cale_sub(self, auto_fixture, a, b, expect):
        """减法"""
        calc = auto_fixture
        assert expect == calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", mul_data, ids=case_name)
    def test_cale_mul(self, auto_fixture, a, b, expect):
        """乘法"""
        calc = auto_fixture
        assert expect == calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", div_data, ids=case_name)
    def test_cale_div(self, auto_fixture, a, b, expect):
        """除法"""
        calc = auto_fixture
        assert expect == calc.div(a, b)
