'''Тесты для словарей (dictionary)'''
import pytest

@pytest.mark.dictionary
class TestDictionary:


    def test_dictionary_sort(self, setup_cars_dictionary):
        '''Проверяем сортировку ключей в словаре'''
        assert (sorted(setup_cars_dictionary.keys())) == ['bmw', 'ford', 'mercedez']

    def test_dictionary_del_key(self, setup_cars_dictionary):
        '''Проверяем удаление ключа'''
        del setup_cars_dictionary['bmw']
        assert setup_cars_dictionary == {'mercedez': 3, 'ford': 2}

    def test_dictionary_contains_element(self, setup_cars_dictionary):
        '''Проверяем после добавления элемента в словарь его наличие'''
        setup_cars_dictionary['mclaren'] = 4
        assert ('mclaren' in setup_cars_dictionary) == 1

    def test_dictionary_pop(self, setup_language_dict):
        '''Заполняем список, очищаем список и проверяем, что список пустой'''
        setup_language_dict.pop(1)
        assert setup_language_dict == {2: 'javascript', 3: 'python', 4: 'php', 5: 'c#'}

    def test_dictionary_clear(self, setup_language_dict):
        '''Проверяем что в словаре удалены все элементы'''
        setup_language_dict.clear()
        assert setup_language_dict == {}
