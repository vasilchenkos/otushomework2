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
    """Проверяем, что длину строку"""
    assert len(setup_string_example) == 11


@pytest.mark.string
def test_string_concatenation(setup_string_example):
    """Проверяем, что множество включает элементы, а значит ненулевое"""
    second_string = "blablabla"
    assert setup_string_example + second_string == "abracadabrablablabla"


@pytest.mark.string
def test_string_count(setup_string_example):
    """Проверяем, что в множествах есть пересекающиеся элементы"""
    assert setup_string_example.count("abra") == 2
