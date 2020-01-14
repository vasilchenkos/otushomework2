import pytest

def test_list_count():
    mobile_vendors = ['apple', 'xiaomi', 'alcatel', 'samsung', 'xiaomi']
    assert mobile_vendors.count('xiaomi') == 2

def test_list_append():
    l = [1,2,3,4,5]
    l.append(6)
    l.append(7)
    l.append(8)
    assert l == [1, 2, 3, 4, 5, 6, 7, 8]

def test_list_index():
    mobile_vendors = ['apple', 'xiaomi', 'alcatel', 'samsung', 'xiaomi']
    assert mobile_vendors.index('apple') == 0

def test_list_sort():
    stack = []
    for x in range(1,11):
        stack.append(x)
    assert stack == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]