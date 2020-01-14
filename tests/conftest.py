import pytest

@pytest.fixture
def setup_vendors(scope='session'):
    mobile_vendors = ['apple', 'xiaomi', 'alcatel', 'samsung', 'xiaomi']