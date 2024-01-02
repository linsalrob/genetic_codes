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
    d = six_frame_translation(seq, 11, False)
    assert len(list(d.keys())) == 21
    assert d['translated_sequence frame +2 2 94'] == 'SIVSMHRIELVRSTSYATYDYASIDQHHYR*'
    assert d['translated_sequence frame +3 3 105'] == 'RSSACIASSSYDRLATLRTTTLASISITIASYDL'
    assert d['translated_sequence frame -2 11 105'] == 'LAIVMLIDASVVVRSVASRSYELDAMHADDR'

if __name__ == "__main__":
    test_translation()
    test_translate_sequence()
