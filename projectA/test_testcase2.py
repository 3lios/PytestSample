import pytest


def test_greater():
    num = 100
    assert num > 100


def test_greater_equal():
    num = 100
    assert num >= 100


def test_less():
    num = 100
    assert num < 200


def equal_test():
    num = 100
    assert num == 100


@pytest.mark.core
def test_core_task3():
    print("here")
    assert 1 == 1


def array_value():
    values = [(1, 11), (2, 22), (3, 35), (4, 44)]
    return values


@pytest.mark.parametrize("num, output", array_value())
def test_mul_11(num, output):
    assert 11 * num == output

