import pytest

@pytest.fixture(scope='session')
def setup_vendors():
    return ['apple', 'xiaomi', 'alcatel', 'samsung', 'xiaomi']

@pytest.fixture(scope='session')
def setup_example_list():
    return [1, 2, 3, 4, 5]
