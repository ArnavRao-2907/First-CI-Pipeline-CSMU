import importlib

module = importlib.import_module("codes.Armstrong_Numbers_29")
is_armstrong = module.is_armstrong

def test_a():
    assert is_armstrong(153) == True

def test_b():
    assert is_armstrong(123) == False

def test_c():
    assert is_armstrong(18) == False

def test_d():
    assert is_armstrong(-60) == False

def test_e():
    assert is_armstrong(0) == True

