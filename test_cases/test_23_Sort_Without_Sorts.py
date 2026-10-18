import importlib

module = importlib.import_module("codes.Sort_Without_Sorts_23")
bubble_sort = module.bubble_sort

def test_a():
    assert bubble_sort([1, 3, 2]) == [1, 2, 3]

def test_b():
    assert bubble_sort([]) == []

def test_c():
    assert bubble_sort([5]) == [5]

def test_d():
    assert bubble_sort([4, 2, 2, 1]) == [1, 2, 2, 4]

def test_e():
    assert bubble_sort([-3, 0, -1, 2]) == [-3, -1, 0, 2]

