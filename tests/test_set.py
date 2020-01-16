'''Тесты для множеств (sets)'''
import pytest

@pytest.mark.sets
class TestSets:

    def test_set_join(self, setup_set_fruits):
        '''Проверяем строку после присоединения к ней другой'''
        assert ('carrot' in setup_set_fruits) == 0


    def test_set_del_element(self):
        '''Проверяем то, что set() удаляет дубликаты элементов множества'''
        test_set_unique = set('airbnbairbnbairbnb')
        assert test_set_unique == {'b', 'n', 'i', 'a', 'r'}

    def test_empty_set(self):
        '''Проверяем, что после создания множества и очистки осталось пустое множество'''
        test_set = {'foo', 'bar'}
        test_set.clear()
        assert test_set == set()

    def test_set_len(self, setup_set_fruits):
        '''Проверяем, что множество включает элементы, а значит ненулевое'''
        assert len(setup_set_fruits) != 0

    def test_set_append(self):
        '''Проверяем, что в множествах есть пересекающиеся элементы'''
        first_set = set('miscrosoft')
        second_set = set('facebook')
        assert(first_set & second_set) == {'f', 'o', 'c'}
