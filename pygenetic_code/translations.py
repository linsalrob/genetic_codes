"""
Translation specific methdos
"""

import PyGeneticCode
from .code_to_table import code_to_table, all_possible_codons
from .dna_and_rna import rna_to_dna
from .error import InvalidCodonException
from .genetic_code import three_letters_to_one_letter



def translate_codon(codon, translation_table=1, one_letter=False):
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
    return amino_acid


def six_frame_translation(dna_sequence, translation_table=11, num_threads=8, verbose=False):
    """
    Translate this sequence in all six frames and return a dictionary of sequences
    :param seq: the sequence to translate
    :param translation_table: the translation table to use (default=11)
    :param num_threads: the number of threads to use for the encoding
    :return: a dictionary of key=seqname value=protein sequences
    """

    verboseInt = 0
    if verbose:
        verboseInt = 1

    return PyGeneticCode.translate(dna_sequence, int(translation_table), num_threads, verboseInt)


if __name__ == '__main__':
    seq = 'ATCGATCGTCAGCATGCATCGCATCGAGCTCGTACGATCGACTAGCTACGCTACGTACGACTACGCTAGCATCGATCAGCATCACTATCGCTAGCTACGATCTA'
    print(f"Translating: {seq}")
    d = six_frame_translation(seq)
    for k in d:
        print(f">{k}\n{d[k]}")
