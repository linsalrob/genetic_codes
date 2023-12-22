"""
Test the genetic codes
"""
from pygenetic_code import genetic_codes

codes = genetic_codes()

def test_codes():
    """
    A simple test for code length
    :return: None
    """
    assert len(codes.keys()) == 25

def test_each_code():
    """
    Make sure each code has 64 codons
    :return: None
    """
    for i in [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]:
        assert len(codes[str(i)]['codons']) == 64


if __name__ == '__main__':
    test_codes()
    test_each_code()
