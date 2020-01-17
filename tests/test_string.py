"""Тесты для строк (string)"""
import pytest


@pytest.mark.string
def test_string_uppercase(setup_string_example):
    """Проверяем, что строка была переведена в верхний регистр"""
    assert setup_string_example.upper() == 'ABRACADABRA'


@pytest.mark.string
def test_string_replace(setup_string_example):
    """Проверяем то, что в строке заменяются буквы"""
    assert setup_string_example.replace("a", "z") == 'zbrzczdzbrz'


@pytest.mark.string
def test_string_len(setup_string_example):
    """Проверяем длину строки"""
    assert len(setup_string_example) == 11


@pytest.mark.string
def test_string_concatenation(setup_string_example):
    """Проверяем, что после конкатенации получилась новая строка"""
    second_string = "blablabla"
    assert setup_string_example + second_string == "abracadabrablablabla"


#@pytest.mark.parametrize('setup_string_example', [("bra")])
@pytest.mark.string
def test_string_count(setup_string_example):
    """Проверяем, количество вхождений в получаемой строке"""
    print(setup_string_example)
    assert setup_string_example.count("abra") == 2
