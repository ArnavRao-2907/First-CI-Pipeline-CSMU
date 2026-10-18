import importlib

module = importlib.import_module("codes.Rotate_Lists_27")
rotate_list = module.rotate_list

def test_a():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_b():
    assert rotate_list([], 3) == []

def test_c():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]

def test_d():
    assert rotate_list([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]

def test_e():
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]

