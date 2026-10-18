import importlib

module = importlib.import_module("codes.Merge_Sorted_List_24")
merge_sorted_lists = module.merge_sorted_lists

def test_a():
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]

def test_b():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]

def test_c():
    assert merge_sorted_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_d():
    assert merge_sorted_lists([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]

def test_e():
    assert merge_sorted_lists([-5, -1, 4], [-3, 0, 6]) == [-5, -3, -1, 0, 4, 6]
