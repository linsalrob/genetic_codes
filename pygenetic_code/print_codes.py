"""
Print the genetic codes in a variety of formats
"""

import argparse

__author__ = 'Rob Edwards'

import sys

from pygenetic_code import genetic_codes


def print_json():
    """
    Print the genetic codes in pretty formatted json
    :return: None
    """

    codes = genetic_codes()

    print("{")
    for i,j in enumerate(codes.keys()):
        print(f"    \"{j}\": ")
        print("        {\n        \"initiators\": ", end="")
        tci = str(codes[j]['initiators']).replace("'", '"')
        print(f"{tci},")
        print("        \"codons\":")
        print("            {")
        n = 0
        for fb in ['A', 'T', 'G', 'C']:
            for sb in ['A', 'T', 'G', 'C']:
                print("            ", end="")
                for tb in ['A', 'T', 'G', 'C']:
                    n+=1
                    codon = fb+sb+tb
                    print(f"\"{codon}\": \"{codes[j]['codons'][codon]}\"", end="")
                    if n < 64:
                        print(", ", end="")
                print()
        print(f"i: {i} len: {len(codes.keys())}", file=sys.stderr)
        if i == len(codes.keys())-1:
            print("            }")
            print("        }")
        else:
            print("            }")
            print("        },")


    print("}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Print the genetic codes')
    parser.add_argument('-j', help='print as json', action='store_true')
    parser.add_argument('-v', help='verbose output', action='store_true')
    args = parser.parse_args()

    if args.j:
        print_json()
