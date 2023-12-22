"""
Test the codon code
"""

from pygenetic_code import codons_to_translation_tables


def test_codons_to_translation_tables():
    """
    We just test the length here
    :return: None
    """
    ctt = codons_to_translation_tables()
    assert len(ctt) == 64



if __name__ == '__main__':
    test_codons_to_translation_tables()
