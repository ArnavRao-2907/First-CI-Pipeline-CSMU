import importlib

module = importlib.import_module("codes.Sum_Of_Lists_26")
sum_of_list = module.sum_of_list

def test_a():
    assert sum_of_list([1, 2, 3, 4]) == 10

def test_b():
    assert sum_of_list([-2,6,9,1.9]) == 14.9

def test_c():
    assert sum_of_list([-15]) == -15

def test_d():
    assert sum_of_list([0]) == 0

def test_e():
    assert sum_of_list([]) == 0

