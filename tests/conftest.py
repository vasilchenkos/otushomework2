"""Соберем setup-методы для использования в тестах"""
import pytest


@pytest.fixture(scope='module')
def setup_vendors_list():
    """Соберем список с вендорами"""
    return ['apple', 'xiaomi', 'alcatel', 'samsung', 'xiaomi']


@pytest.fixture(scope='module')
def setup_example_list():
    """Соберем список с цифрами"""
    return [1, 2, 3, 4, 5]


@pytest.fixture(scope='module')
def setup_cars_dictionary():
    """Соберем список со словарем машин"""
    return {'bmw': 1, 'mercedez': 3, 'ford': 2}


@pytest.fixture(scope='module')
def setup_language_dict():
    """Соберем список со словарем языков программирования"""
    return {1: 'java', 2: 'javascript', 3: 'python', 4: 'php', 5: 'c#'}


@pytest.fixture(scope='module')
def setup_set_fruits():
    """Соберем список со словарем языков программирования"""
    return {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
