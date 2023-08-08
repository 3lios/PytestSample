import pytest


def test_diff():
    num = 100
    assert num == 200


@pytest.mark.core
def test_core_task2():
    assert 1 == 2


@pytest.mark.div
def test_divisible_by_13(input_value):
    assert input_value % 13 == 0

