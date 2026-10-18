import importlib

module = importlib.import_module("codes.Largest__Words_21")
largest_word = module.largest_word

def test_a():
    assert largest_word("I love programming and coding") == "programming"
    
def test_b():
    assert largest_word("Welcome, world!") == "Welcome"
    
def test_c():
    assert largest_word("cat dog bat") == "cat"
    
def test_d():
    assert largest_word("Python") == "Python"
    
def test_e():
    assert largest_word("") == ""
