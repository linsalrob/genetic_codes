from pygenetic_code import code_to_table


def test_trans_table(trans=11):
    # trans 11 is bacteria
    code = code_to_table(trans)
    assert sorted(code['initiators']) == ['ATA', 'ATC', 'ATG', 'ATT', 'CTG', 'GTG', 'TTG']
    assert len(code['codons']) == 64


def test_table_ten(trans=10):
    # trans 10 is The Euplotid Nuclear Code. This has UGA as Cys
    code = code_to_table(trans)
    assert code['initiators'] == ['ATG']
    assert len(code['codons']) == 64
    assert code['codons']['TGA'] == 'Cys'


def test_table_five(trans=5):
    # trans 5. The Invertebrate Mitochondrial Code (transl_table=5)
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
