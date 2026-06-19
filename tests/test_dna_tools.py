from dna_tools import gc_percentage

def test_gc_percentage():
    assert gc_percentage(["G","C","G","C"]) == 100
    assert gc_percentage(["A","T","A","T"]) == 0
