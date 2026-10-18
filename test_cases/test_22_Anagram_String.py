import importlib

module = importlib.import_module("codes.Anagram_String_22")
is_anagram = module.is_anagram

def test_a():
    assert is_anagram("List", "Lost") == False

def test_b():
	assert is_anagram("Listen", "Silent") == True

def test_c():
    assert is_anagram("Tc", "Ttc") == False

def test_d():
    assert is_anagram("Listen", "lisTen") == True

def test_e():
    assert is_anagram("-2s", "s-2") == True

