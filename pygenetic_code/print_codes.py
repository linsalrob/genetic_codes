"""
Print the genetic codes in a variety of formats
"""

import argparse
import sys

from pygenetic_code import genetic_codes, all_possible_codons
from pygenetic_code.genetic_code import three_letters_to_one_letter


def print_json():
    """
    Print the genetic codes in pretty formatted json
    :return: None
    """

    codes = genetic_codes()

    print("{")
    for i, j in enumerate(codes.keys()):
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
                    n += 1
                    codon = fb + sb + tb
                    print(f"\"{codon}\": \"{codes[j]['codons'][codon]}\"", end="")
                    if n < 64:
                        print(", ", end="")
                print()
        print(f"i: {i} len: {len(codes.keys())}", file=sys.stderr)
        if i == len(codes.keys()) - 1:
            print("            }")
            print("        }")
        else:
            print("            }")
            print("        },")
    print("}")


def print_difference_to_maximum():
    """
    Print the difference table
    :return: None
    """
    codes = genetic_codes()

    # find the most abundant amino acid for each codon
    counts = {x: {} for x in all_possible_codons()}
    for tt in codes:
        for codon in all_possible_codons():
            aa = codes[tt]['codons'][codon]
            counts[codon][aa] = counts[codon].get(aa, 0) + 1

    # maxes is a dict of each codon and the most abundant translation
    maxes = {x: max(counts[x], key=counts[x].get) for x in counts}

    all_codes = sorted(genetic_codes().keys(), key=lambda x: int(x))
    print("\t".join(["Codon", "Translation"] + all_codes))
    for cd in all_possible_codons():
        print(cd, end="\t")
        print(maxes[cd], end="")
        for tt in all_codes:
            if codes[tt]['codons'][cd] == maxes[cd]:
                print("\t-", end="")
            else:
                print(f"\t{codes[tt]['codons'][cd]}", end="")
        print()


def print_difference_to_code_one():
    """
    Print the difference table between all translations and code 1
    :return: None
    """
    codes = genetic_codes()

    all_codes = sorted(genetic_codes().keys(), key=lambda x: int(x))
    print("\t".join(["Codon", "Translation"] + all_codes))
    for cd in all_possible_codons():
        print(cd, end="\t")
        print(codes["1"]['codons'][cd], end="")
        for tt in all_codes:
            if codes["1"]['codons'][cd] == codes[tt]['codons'][cd]:
                print("\t-", end="")
            else:
                print(f"\t{codes[tt]['codons'][cd]}", end="")
        print()

def print_table():
    """
    Print a look up table for all the genetic codes as a C-style list of lists, and then print a look up table
    for the codons
    :return: None
    """

    codes = genetic_codes()
    all_codons = sorted(all_possible_codons())
    tto = three_letters_to_one_letter()

    print("{")
    for tt in range(32):
        print("{", end="")
        if str(tt) in codes:
            for i, codon in enumerate(all_codons):
                aa = tto[codes[str(tt)]['codons'][codon]]
                print(f"'{aa}'", end="")
                if i < len(all_codons) - 1:
                    print(", ", end="")
            print("}, // genetic code " + f"{tt}")
        else:
            print("},")
    print("}\n")
    








if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Print the genetic codes')
    parser.add_argument('-j', help='print as json', action='store_true')
    parser.add_argument('-d', help='print difference from translation table 1', action='store_true')
    parser.add_argument('-x', help='print difference from the most common codon usage', action='store_true')
    parser.add_argument('-t', help='print a table', action='store_true')
    parser.add_argument('-v', help='verbose output', action='store_true')
    args = parser.parse_args()

    if args.j:
        print_json()
    if args.d:
        print_difference_to_code_one()
    if args.x:
        print_difference_to_maximum()
    if args.t:
        print_table()
