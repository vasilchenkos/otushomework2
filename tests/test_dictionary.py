'''Тесты для словарей (dictionary)'''

def test_dictionary_sort():
    '''Проверяем сортировку ключей в словаре'''
    cars = {'bmw': 1, 'mercedez': 3, 'ford': 2}
    assert (sorted(cars.keys())) == ['bmw', 'ford', 'mercedez']

def test_dictionary_del_key():
    '''Проверяем удаление ключа'''
    cars = {'bmw': 1, 'mercedez': 3, 'ford': 2}
    del cars['bmw']
    assert cars == {'mercedez': 3, 'ford': 2}

def test_dictionary_contains_element():
    '''Проверяем после добавления элемента в словарь его наличие'''
    cars = {'bmw': 1, 'mercedez': 3, 'ford': 2}
    cars['mclaren'] = 4
    assert ('mclaren' in cars) == 1

def test_dictionary_pop():
    '''Заполняем список, очищаем список и проверяем, что список пустой'''
    dict_trips = {1: 'oneway', 2: 'roundtrip', 3: 'transfer'}
    dict_trips.pop(1)
    assert dict_trips == {2: 'roundtrip', 3: 'transfer'}

def test_dictionary_clear():
    '''Проверяем что в словаре удалены все элементы'''
    language_dict = {1: 'java', 2: 'javascript', 3: 'python', 4: 'php', 5: 'c#'}
    language_dict.clear()
    assert language_dict == {}
