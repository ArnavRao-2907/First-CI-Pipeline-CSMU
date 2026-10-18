import importlib

module = importlib.import_module("codes.Decimal_To_Binarys_30")
decimal_to_binary = module.decimal_to_binary

def test_a():
    assert decimal_to_binary(10) == '1010'

def test_b():
    assert decimal_to_binary(111) == '1101111'

def test_c():
    assert decimal_to_binary(0) == '0'

def test_d():
    assert decimal_to_binary(-9) == '-1001'

def test_e():
    assert decimal_to_binary(82) == '1010010'

