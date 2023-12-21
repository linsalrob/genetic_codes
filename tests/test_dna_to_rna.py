"""
A really simple test!
"""

from pygenetic_code import rna_to_dna, dna_to_rna


def test_rna_to_dna():
    assert rna_to_dna('UGA') == 'TGA'
    assert rna_to_dna('AGU') == 'AGT'
    assert rna_to_dna('UUU') == 'TTT'


def test_dna_to_rna():
    assert dna_to_rna('TGA') == 'UGA'
    assert dna_to_rna('AGT') == 'AGU'
    assert dna_to_rna('TTT') == 'UUU'


if __name__ == "__main__":
    test_rna_to_dna()
    test_dna_to_rna()
