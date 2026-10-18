import importlib

module = importlib.import_module("codes.Set_Intersections_28")
set_intersection = module.set_intersection

def test_a():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == [2, 3]

def test_b():
    assert set_intersection([], [1, 2, 3]) == []

def test_c():
    assert set_intersection([1, 2], [3, 4]) == []

def test_d():
    assert set_intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3]

def test_e():
    assert set_intersection([4, 5, 6], [6, 5, 4]) == [4, 5, 6]
