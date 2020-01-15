'''Тесты для словарей (dictionary)'''

def test_dictionary_sort(setup_cars_dictionary):
    '''Проверяем сортировку ключей в словаре'''
    assert (sorted(setup_cars_dictionary.keys())) == ['bmw', 'ford', 'mercedez']

def test_dictionary_del_key(setup_cars_dictionary):
    '''Проверяем удаление ключа'''
    del setup_cars_dictionary['bmw']
    assert setup_cars_dictionary == {'mercedez': 3, 'ford': 2}

def test_dictionary_contains_element(setup_cars_dictionary):
    '''Проверяем после добавления элемента в словарь его наличие'''
    #cars = {'bmw': 1, 'mercedez': 3, 'ford': 2}
    setup_cars_dictionary['mclaren'] = 4
    assert ('mclaren' in setup_cars_dictionary) == 1

def test_dictionary_pop(setup_language_dict):
    '''Заполняем список, очищаем список и проверяем, что список пустой'''
    setup_language_dict.pop(1)
    assert setup_language_dict == {2: 'javascript', 3: 'python', 4: 'php', 5: 'c#'}

def test_dictionary_clear(setup_language_dict):
    '''Проверяем что в словаре удалены все элементы'''
    setup_language_dict.clear()
    assert setup_language_dict == {}
