from validators import is_valid

def test_valid_sequence():
    assert is_valid(["A","T","G","C"]) == True

def test_invalid_base():
    assert is_valid(["A","B","C"]) == False

def test_rna_warning():
    assert is_valid(["A","U","G"]) == False
