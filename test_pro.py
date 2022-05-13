import pytest


def test_pro():

    print("这是一个测试用例")


if __name__ == '__main__':
    # pytest.main(['test_pro.py'])
    pytest.main(["--alluredir=allure_result"])