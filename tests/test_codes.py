"""
Test the genetic codes
"""
from pygenetic_code import genetic_codes, translation_tables

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
    for i in translation_tables():
        assert len(codes[str(i)]['codons']) == 64


def test_translation_tables():
    """
    Test the translation tables and make sure we have the right number
    :return: None
    """

    tt = translation_tables()
    assert len(tt) == 25


if __name__ == '__main__':
    test_codes()
    test_each_code()
    test_translation_tables()
