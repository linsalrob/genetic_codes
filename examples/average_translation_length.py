"""
Calculate the min, max, mean, and modal translation length for a DNA
sequence using different translation tables
"""

import sys
import argparse
from pygenetic_code import translation_tables, six_frame_translation
from examples.example_lib import stream_fasta, mean, median

__author__ = 'Rob Edwards'


def calculate_statistics(fafile, verbose=False):
    """
    Calculate min, max, mean, mode for translations using all the translation tables
    :param fafile: Fasta file
    :param verbose: more output
    :return: None
    """

    valid_translation_tables = translation_tables()

    print("Sequence\tTranslation table\tNumber of ORFs\tShortest\tLongest\tMean\tMedian")

    for seqid, seq in stream_fasta(fafile, False):
        for tt in valid_translation_tables:
            if verbose:
                print(f"Translating {seqid} using translation table {tt}", file=sys.stderr)
            trans = six_frame_translation(seq, tt)
            lengths = [len(x) for x in trans.values()]
            print("\t".join(map(str, [seqid, tt, len(lengths), min(lengths), max(lengths), mean(lengths),
                                      median(lengths)])))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate some statistics about the translations')
    parser.add_argument('-f', help='DNA fasta file', required=True)
    parser.add_argument('-v', help='verbose output', action='store_true')
    args = parser.parse_args()

    calculate_statistics(args.f, args.v)
