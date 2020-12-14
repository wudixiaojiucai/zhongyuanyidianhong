import pytest
from pythoncode.calculator import Calculator


@pytest.fixture(scope="module")
def auto_fixture():
    calc = Calculator()
    print("测试用例开始执行")
    yield calc
    print("测试用例执行结束")
