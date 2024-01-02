"""
Test the translation functions
"""
from pygenetic_code.translations import translate_codon, six_frame_translation


def test_translation():
    """
    Can we properly translate?
    :return: None
    """
    assert translate_codon('ATG', 1, False) == 'Met'
    assert translate_codon('TGA', 21, False) == 'Trp'
    assert translate_codon('TGA', 1, False) == 'Ter'
    assert translate_codon('TGA', 1, True) == '*'
    assert translate_codon('ATG', 1, True) == 'M'


def test_translate_sequence():
    """
    Can we translate a big sequence?
    :return:
    """
    seq = 'ATCGATCGTCAGCATGCATCGCATCGAGCTCGTACGATCGACTAGCTACGCTACGTACGACTACGCTAGCATCGATCAGCATCACTATCGCTAGCTACGATCTA'
    print(f"Translating: {seq}")
    d = six_frame_translation(seq)
    for k in d:
        print(f">{k}\n{d[k]}")

if __name__ == "__main__":
    test_translation()
    test_translate_sequence()
