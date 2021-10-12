import pytest
@pytest.fixture()
def test_01():
    a = 5
    return a

def test_02(test_01):
    assert test_01 == 5
    print("断言成功")


@pytest.fixture()
def test_03():
    a = 5
    b = 6
    return (a, b)


def test_04(test_03):
    a = test_03[0]
    b = test_03[1]
    assert a < b
    print("断言成功")