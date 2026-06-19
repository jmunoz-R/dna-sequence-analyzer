from dna_tools import gc_percentage

def test_gc_percentage():
    assert gc_percentage(["G","C","G","C"]) == 100
    assert gc_percentage(["A","T","A","T"]) == 0

def test_gc():
    assert gc_percentage(["G","C","G","C"]) == 100
    assert gc_percentage(["A","T","A","T"]) == 0

def test_complement():
    assert get_complementary_strand(["A","T","C"]) == ["T","A","G"]

def test_reverse_complement():
    assert reverse_complement(["T","A","G"]) == ["G","A","T"]

def test_translation():
    assert translate(["A","T","G"]) == ["Met"]
