def test_list_count():
    '''Проверяем в тесте сколько раз был добавлен элемент в списке'''
    mobile_vendors = ['apple', 'xiaomi', 'alcatel', 'samsung', 'xiaomi']
    assert mobile_vendors.count('xiaomi') == 2

def test_list_append():
    '''Добавляем в список элементы и сравниваем добавились элементы в конце или нет'''
    test_l = [1, 2, 3, 4, 5]
    test_l.append(6)
    test_l.append(7)
    test_l.append(8)
    assert test_l == [1, 2, 3, 4, 5, 6, 7, 8]

def test_list_index():
    '''Проверяем в тесте индекс элемента'''
    mobile_vendors = ['apple', 'xiaomi', 'alcatel', 'samsung', 'xiaomi']
    assert mobile_vendors.index('apple') == 0

def test_list_clear():
    '''Заполняем список, очищаем список и проверяем что список пустой'''
    stack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    stack.clear()
    assert stack == []

def test_list_remove():
    '''Удаляем конкретный элемент в списке и проверяем список'''
    example_list = [1, 2, 3, 4, 5]
    example_list.remove(2)
    assert example_list == [1, 3, 4, 5]