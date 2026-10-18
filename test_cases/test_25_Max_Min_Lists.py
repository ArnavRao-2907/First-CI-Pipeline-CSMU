import importlib

module = importlib.import_module("codes.Max_Min_Lists_25")
find_max_min = module.find_max_min

def test_a():
    assert find_max_min([4, 9, 1, 7]) == (9, 1)

def test_b():
    assert find_max_min([10, 2, 8, 6]) == (10, 2)

def test_c():
    assert find_max_min([-5, -2, -8]) == (-2, -8)

def test_d():
    assert find_max_min([7]) == (7, 7)

def test_e():
    assert find_max_min([]) == None

