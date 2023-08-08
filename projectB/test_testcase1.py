import pytest


@pytest.mark.core
def test_core_task1():
    assert 1 == 1


class TestCls:
    @staticmethod
    def value():
        return 123

    @pytest.mark.cls
    def test_cls_task1(self):
        assert 123 > self.value()

    @pytest.mark.cls
    def test_cls_task2(self):
        assert 1 == 1


