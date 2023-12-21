"""
Translation specific methdos
"""

from .code_to_table import code_to_table, all_possible_codons
from .dna_and_rna import rna_to_dna
from .Error import InvalidCodonException
from .genetic_code import three_letters_to_one_letter


def translate(codon, translation_table=1, one_letter=False):
    """
    Translate a codon given a specific translation table.
    :param codon: the codon to translate
    :param translation_table: the translation table to use
    :param one_letter: return the one letter amino acid abbreviation
    :return: the amino acid abbreviation
    """

    if 'U' in codon:
        codon = rna_to_dna(codon)

    if codon not in all_possible_codons():
        raise InvalidCodonException(f"{codon} is not a valid codon. It should be one of {all_possible_codons()}")

    code = code_to_table(translation_table)
    amino_acid = code['codons'][codon]
    if one_letter:
        return three_letters_to_one_letter()[amino_acid]
    else:
        return amino_acid

