"""Тесты для строк (string)"""
import pytest


@pytest.mark.string
def test_string_join(setup_string_example):
    """Проверяем, что строка была переведена в верхний регистр"""
    assert setup_string_example.upper() == 'ABRACADABRA'

    # assert str == setup_string_example + example_string
#
#
# def test_string():
#     '''Проверяем то, что set() удаляет дубликаты элементов множества'''
#     test_set_unique = set('airbnbairbnbairbnb')
#     assert test_set_unique == {'b', 'n', 'i', 'a', 'r'}
#
# def test_string():
#     '''Проверяем, что после создания множества и очистки осталось пустое множество'''
#     test_set = {'foo', 'bar'}
#     test_set.clear()
#     assert test_set == set()
#
# def test_string():
#     '''Проверяем, что множество включает элементы, а значит ненулевое'''
#     fruits = {'apple', 'pear', 'orange', 'banana'}
#     assert len(fruits) != 0
#
# def test_string():
#     '''Проверяем, что в множествах есть пересекающиеся элементы'''
#     first_set = set('miscrosoft')
#     second_set = set('facebook')
#     assert(first_set & second_set) == {'f', 'o', 'c'}
