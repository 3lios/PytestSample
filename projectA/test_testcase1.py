import math
import pytest


# @pytest.mark.skip
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


# @pytest.mark.xfail
def testsquare():
    num = 7
    assert 7*7 == 40


def tesequality():
    assert 10 == 11


@pytest.mark.div
def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


@pytest.mark.div
def test_divisible_by_6(input_value):
    assert input_value % 6 == 0

