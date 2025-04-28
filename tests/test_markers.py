import pytest


@pytest.mark.smoke
def test_some_case():
    pass


@pytest.mark.regression
def test_some_case():
    pass


@pytest.mark.smoke
class TestSuite:
    @pytest.mark.smoke
    def test_case1(self):
        pass

    def test_case2(self):
        pass


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
def test_critical_login():
    pass
