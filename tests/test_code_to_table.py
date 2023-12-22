"""
Test the code to table code
"""

from pygenetic_code import code_to_table


def test_trans_table(trans=11):
    """
    translation code 11 is bacteria
    :param trans: the translation code
    :return: None
    """
    code = code_to_table(trans)
    assert sorted(code['initiators']) == ['ATA', 'ATC', 'ATG', 'ATT', 'CTG', 'GTG', 'TTG']
    assert len(code['codons']) == 64


def test_table_ten(trans=10):
    """
    translation code 10 is The Euplotid Nuclear Code. This has UGA as Cys
    :param trans: the translation code
    :return: None
    """
    code = code_to_table(trans)
    assert code['initiators'] == ['ATG']
    assert len(code['codons']) == 64
    assert code['codons']['TGA'] == 'Cys'


def test_table_five(trans=5):
    """
    translation code 5. The Invertebrate Mitochondrial Code (transl_table=5)
    :param trans: the translation code
    :return: None
    """
    code = code_to_table(trans)
    assert sorted(code['initiators']) == ['ATA', 'ATC', 'ATG', 'ATT', 'GTG', 'TTG']
    assert len(code['codons']) == 64
    assert code['codons']['AGA'] == 'Ser'
    assert code['codons']['AGG'] == 'Ser'
    assert code['codons']['ATA'] == 'Met'
    assert code['codons']['TGA'] == 'Trp'


if __name__ == '__main__':
    test_trans_table()
    test_table_ten()
    test_table_five()
