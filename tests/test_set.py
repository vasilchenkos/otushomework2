"""Тесты для множеств (sets)"""
import pytest


@pytest.mark.sets
def test_set_join(setup_set_fruits):
    """Проверяем строку после присоединения к ней другой"""
    assert ('carrot' in setup_set_fruits) == 0


@pytest.mark.sets
def test_set_del_element():
    """Проверяем то, что set() удаляет дубликаты элементов множества"""
    test_set_unique = set('airbnbairbnbairbnb')
    assert test_set_unique == {'b', 'n', 'i', 'a', 'r'}


@pytest.mark.sets
def test_empty_set():
    """Проверяем, что после создания множества и очистки осталось пустое множество"""
    test_set = {'foo', 'bar'}
    test_set.clear()
    assert test_set == set()


@pytest.mark.sets
def test_set_len(setup_set_fruits):
    """Проверяем, что множество включает элементы, а значит ненулевое"""
    assert len(setup_set_fruits) != 0


@pytest.mark.sets
def test_set_append():
    """Проверяем, что в множествах есть пересекающиеся элементы"""
    first_set = set('miscrosoft')
    second_set = set('facebook')
    assert (first_set & second_set) == {'f', 'o', 'c'}


TESTDATA = [
    ({'foo', 'bar'}, None),
    ({'ololo'}, None),
]


@pytest.mark.sets
@pytest.mark.parametrize("set_example, expected", TESTDATA)
def test_count_string(set_example, expected):
    """Очищаем множество элементов"""
    assert set_example.clear() == expected
