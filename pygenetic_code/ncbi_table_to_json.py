"""
Parse the NCBI Table that is, by default in codes/ncbi_tables.txt and create a json object
"""
import json
import os
import sys
import argparse
import re

__author__ = 'Rob Edwards'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse the NCBI Table')
    parser.add_argument('-f', help='input file', default='../codes/ncbi_tables.txt')
    parser.add_argument('-v', help='verbose output', action='store_true')
    args = parser.parse_args()

    head = re.compile(r'transl_table=(\d+)')
    table = re.compile(r'\w\w\w\s+')

    trans_table = None
    data = {}
    initiators = None
    codons = None
    with open(args.f, 'r') as f:
        for l in f:
            if (l.startswith('#')):
                continue
            l = l.strip()
            if not l:
                continue
            m = head.search(l)
            if m:
                if codons:
                    data[trans_table] = {'initiators': list(initiators), 'codons': codons}
                trans_table = int(m.groups()[0])
                initiators = set()
                codons = {}
            elif table.match(l):
                p = l.strip().split()
                i = 0
                while i < len(p):
                    codon = p[i]
                    i += 2
                    if codon in codons:
                        print(
                            f"For the codon {codon} in trans table {trans_table} we already had {codons[codon]} but now "
                            f"we found {p[i]}", file=sys.stderr)
                    codons[codon] = p[i]
                    i += 1
                    if i < len(p) and p[i] == 'i':
                        initiators.add(codon)
                        i += 1
            else:
                print(f"ERROR: We don't know what {l} means?", file=sys.stderr)

    print(json.dumps(data))
