"""
Of course, codons are translated in RNA, but we always work in DNA space. This is a simple function that
converts DNA -> RNA or vice versa.
"""


def dna_to_rna(dna):
    """
    Convert a DNA string to an RNA string
    :param dna: A DNA string
    :return: An RNA string
    """
    return dna.replace('T', 'U')


def rna_to_dna(rna):
    """
    Convert a RNA string to a DNA string
    :param dna: A RNA string
    :return: An DNA string
    """
    return rna.replace('U', 'T')
