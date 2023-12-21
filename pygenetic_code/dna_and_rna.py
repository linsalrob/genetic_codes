"""
Of course, codons are translated in RNA, but we always work in DNA space. This is a simple function that
converts DNA -> RNA or vice versa.
"""


def dna_to_rna(dna):
    return dna.replace('T', 'U')


def rna_to_dna(rna):
    return rna.replace('U', 'T')
