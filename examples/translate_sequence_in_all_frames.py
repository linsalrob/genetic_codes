"""
Translate one sequence with one translation table
"""

import argparse
import PyGeneticCode
from example_lib import stream_fasta

__author__ = 'Rob Edwards'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Translate one sequence')
    parser.add_argument('-f', help='fasta DNA file', required=True)
    parser.add_argument('-t', help='translation table', required=True, type=int)
    parser.add_argument('-j', help='number of threads (default=8)', type=int, default=8)
    parser.add_argument('-v', help='verbose output', action='store_true')
    args = parser.parse_args()

    for seqid, dna_sequence in stream_fasta(args.f):
        try:
            translations = PyGeneticCode.translate_six_frames(dna_sequence, args.t, args.j, args.v)
            for name in translations:
                print(f">{name}\n{translations[name]}")
        except ValueError as e:
            print("Incorrect parameter passed to the code: ")
            print(e)
