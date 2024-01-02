"""
Re-encode the codons using two bit encoding

A: 00
C: 01
G: 10
T: 11
"""

import argparse

__author__ = 'Rob Edwards'

from pygenetic_code import all_possible_codons


def encode_codons():
    """
    A simple routine to print out some codons encoded in two bit binary format
    :return: None
    """
    codons = sorted(all_possible_codons())
    code = {'A': "00", "C": "01", "G": "10", "T": "11"}
    for c in codons:
        bi = f"{code[c[0]]}{code[c[1]]}{code[c[2]]}"
        print(f"{c}\t{bi}\t{int(bi, 2)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Encode the codons')
    parser.add_argument('-v', help='verbose output', action='store_true')
    args = parser.parse_args()

    encode_codons()
