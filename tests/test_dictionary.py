"""Тесты для словарей (dictionary)"""
import pytest


@pytest.mark.dictionary
def test_dictionary_sort(setup_cars_dictionary):
    """Проверяем сортировку ключей в словаре"""
    assert (sorted(setup_cars_dictionary.keys())) == ['bmw', 'ford', 'mercedez']


@pytest.mark.dictionary
def test_dictionary_del_key(setup_cars_dictionary):
    """Проверяем удаление ключа"""
    del setup_cars_dictionary['bmw']
    assert setup_cars_dictionary == {'mercedez': 3, 'ford': 2}


@pytest.mark.dictionary
def test_dictionary_contains_element(setup_cars_dictionary):
    """Проверяем после добавления элемента в словарь его наличие"""
    setup_cars_dictionary['mclaren'] = 4
    assert ('mclaren' in setup_cars_dictionary) == 1


@pytest.mark.dictionary
def test_dictionary_pop(setup_language_dict):
    """Заполняем список, убираем элемент по ключу и проверяем список"""
    setup_language_dict.pop(1)
    assert setup_language_dict == {2: 'javascript', 3: 'python', 4: 'php', 5: 'c#'}


@pytest.mark.dictionary
def test_dictionary_clear(setup_language_dict):
    """Проверяем, что в словаре удалены все элементы"""
    setup_language_dict.clear()
    assert setup_language_dict == {}


TESTDATA = [
    ({1: 'java', 2: 'javascript', 3: 'python'}, 1, 'java'),
    ({1: 'bmw', 3: "mercedez", 2: 'ford'}, 3, 'mercedez'),
    ({1: 'java', 2: 'javascript', 3: 'python'}, 2, 'javascript'),
]


@pytest.mark.parametrize("dict_example, number,  expected", TESTDATA)
@pytest.mark.dictionary
def test_dictionary_clear(dict_example, number, expected):
    """Проверяем что в словаре удалены все элементы"""
    assert dict_example.pop(number) == expected
