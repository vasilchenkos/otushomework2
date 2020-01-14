import pytest

@pytest.fixture()
def test_list():
    mobile_vendors = ['apple', 'xiaomi', 'alcatel', 'samsung', 'xiaomi']
    assert mobile_vendors.reverse() == ['xiaomi', 'samsung', 'alcatel', 'xiaomi', 'apple']
