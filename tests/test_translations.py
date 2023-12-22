"""
Test the translation functions
"""
from pygenetic_code.translations import translate


def test_translation():
    assert translate('ATG', 1, False) == 'Met'
    assert translate('TGA', 21, False) == 'Trp'
    assert translate('TGA', 1, False) == 'Ter'
    assert translate('TGA', 1, True) == '*'
    assert translate('ATG', 1, True) == 'M'

if __name__ == "__main__":
    test_translation()