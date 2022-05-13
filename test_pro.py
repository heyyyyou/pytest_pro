import pytest


def test_pro():

    print("999")


if __name__ == '__main__':
    # pytest.main(['test_pro.py'])
    pytest.main(["--alluredir=allure-results"])