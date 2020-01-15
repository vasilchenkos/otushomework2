# '''Тесты для множеств (sets)'''
#
# def test_set_contains_element():
#     '''Проверяем содержит ли множество элемент'''
#     fruits = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
#     assert ('carrot' in fruits) == 0
#
#
# def test_set_del_element():
#     '''Проверяем то, что set() удаляет дубликаты элементов множества'''
#     test_set_unique = set('airbnbairbnbairbnb')
#     assert test_set_unique == {'b', 'n', 'i', 'a', 'r'}
#
#
# def test_empty_set():
#     '''Проверяем, что после создания множества и очистки осталось пустое множество'''
#     test_set = {'foo', 'bar'}
#     test_set.clear()
#     assert test_set == set()
#
# def test_set_len():
#     '''Проверяем, что множество включает элементы, а значит ненулевое'''
#     fruits = {'apple', 'pear', 'orange', 'banana'}
#     assert len(fruits) != 0
#
#
#
# def test_set_append():
#     '''Проверяем, что в множествах есть пересекающиеся элементы'''
#     first_set = set('miscrosoft')
#     second_set = set('facebook')
#     assert(first_set & second_set) == {'f', 'o', 'c'}
#
