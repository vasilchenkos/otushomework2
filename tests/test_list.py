"""Тест для списков (list)"""
import pytest


@pytest.mark.list
def test_list_count(setup_vendors_list):
    """Проверяем в тесте сколько раз был добавлен элемент в списке"""
    assert setup_vendors_list.count('xiaomi') == 2


@pytest.mark.list
def test_list_append(setup_example_list):
    """Добавляем в список элементы и сравниваем добавились элементы в конце списка или нет"""
    setup_example_list.append(6)
    setup_example_list.append(7)
    setup_example_list.append(8)
    assert setup_example_list == [1, 2, 3, 4, 5, 6, 7, 8]


@pytest.mark.list
def test_list_index(setup_vendors_list):
    """Проверяем в тесте индекс элемента"""
    assert setup_vendors_list.index('apple') == 0


@pytest.mark.list
def test_list_clear(setup_example_list):
    """Заполняем список, очищаем список и проверяем, что список пустой"""
    setup_example_list.clear()
    assert setup_example_list == []


@pytest.mark.list
def test_list_remove(setup_vendors_list):
    """Проверяем список после удаления элемента"""
    setup_vendors_list.remove('xiaomi')
    assert setup_vendors_list == ['apple', 'alcatel', 'samsung', 'xiaomi']
