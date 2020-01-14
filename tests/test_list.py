import pytest
import allure
def test_sun():
    assert 2+3 == 5

def test_division():
    #assert 2/0 == 1
    with pytest.raises(ZeroDivisionError):
        print(4/0)


