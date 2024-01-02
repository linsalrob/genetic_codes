"""
Module to handle exporting the genetic codes
"""

import json



def genetic_codes():
    """
    The genetic codes. This has been imported from codes/ncbi.json, and is provided
    to hopefully make things slightly faster than reading that file
    :return: a dictionary of translation tables, their initiators, and their codons
    """
    return json.loads(
            '''
{
"1":
{
    "initiators": ["TTG", "CTG", "ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Ter", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"2":
{
    "initiators": ["GTG", "ATC", "ATA", "ATT", "ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Met", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Ter", "AGT": "Ser", "AGG": "Ter", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Trp", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"3":
{
    "initiators": ["ATA", "ATG", "GTG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Met", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Trp", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Thr", "CTT": "Thr", "CTG": "Thr", "CTC": "Thr",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"4":
{
    "initiators": ["GTG", "TTA", "ATC", "ATA", "ATT", "TTG", "CTG", "ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Trp", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"5":
{
    "initiators": ["GTG", "ATC", "ATA", "ATT", "TTG", "ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Met", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Ser", "AGT": "Ser", "AGG": "Ser", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Trp", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"6":
{
    "initiators": ["ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Gln", "TAT": "Tyr", "TAG": "Gln", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Ter", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"9":
{
    "initiators": ["ATG", "GTG"],
    "codons":
        {
            "AAA": "Asn", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Ser", "AGT": "Ser", "AGG": "Ser", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Trp", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"10":
{
    "initiators": ["ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Cys", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"11":
{
    "initiators": ["GTG", "ATC", "ATA", "ATT", "TTG", "CTG", "ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Ter", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"12":
{
    "initiators": ["CTG", "ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Ter", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Ser", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"13":
{
    "initiators": ["TTG", "ATA", "ATG", "GTG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Met", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Gly", "AGT": "Ser", "AGG": "Gly", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Trp", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"14":
{
    "initiators": ["ATG"],
    "codons":
        {
            "AAA": "Asn", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Ser", "AGT": "Ser", "AGG": "Ser", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Tyr", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Trp", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"15":
{
    "initiators": ["ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Gln", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Ter", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"16":
{
    "initiators": ["ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Leu", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Ter", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"21":
{
    "initiators": ["ATG", "GTG"],
    "codons":
        {
            "AAA": "Asn", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Met", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Ser", "AGT": "Ser", "AGG": "Ser", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Trp", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"22":
{
    "initiators": ["ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Leu", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Ter", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ter", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"23":
{
    "initiators": ["ATG", "ATT", "GTG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Ter", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Ter", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"24":
{
    "initiators": ["TTG", "CTG", "ATG", "GTG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Ser", "AGT": "Ser", "AGG": "Lys", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Trp", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"25":
{
    "initiators": ["TTG", "ATG", "GTG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Gly", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"26":
{
    "initiators": ["CTG", "ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Ter", "TAT": "Tyr", "TAG": "Ter", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Ter", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Ala", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"27":
{
    "initiators": ["ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Gln", "TAT": "Tyr", "TAG": "Gln", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Trp", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"28":
{
    "initiators": ["ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Gln", "TAT": "Tyr", "TAG": "Gln", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Trp", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"29":
{
    "initiators": ["ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Tyr", "TAT": "Tyr", "TAG": "Tyr", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Ter", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"30":
{
    "initiators": ["ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Glu", "TAT": "Tyr", "TAG": "Glu", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Ter", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
},
"31":
{
    "initiators": ["ATG"],
    "codons":
        {
            "AAA": "Lys", "AAT": "Asn", "AAG": "Lys", "AAC": "Asn",
            "ATA": "Ile", "ATT": "Ile", "ATG": "Met", "ATC": "Ile",
            "AGA": "Arg", "AGT": "Ser", "AGG": "Arg", "AGC": "Ser",
            "ACA": "Thr", "ACT": "Thr", "ACG": "Thr", "ACC": "Thr",
            "TAA": "Glu", "TAT": "Tyr", "TAG": "Glu", "TAC": "Tyr",
            "TTA": "Leu", "TTT": "Phe", "TTG": "Leu", "TTC": "Phe",
            "TGA": "Trp", "TGT": "Cys", "TGG": "Trp", "TGC": "Cys",
            "TCA": "Ser", "TCT": "Ser", "TCG": "Ser", "TCC": "Ser",
            "GAA": "Glu", "GAT": "Asp", "GAG": "Glu", "GAC": "Asp",
            "GTA": "Val", "GTT": "Val", "GTG": "Val", "GTC": "Val",
            "GGA": "Gly", "GGT": "Gly", "GGG": "Gly", "GGC": "Gly",
            "GCA": "Ala", "GCT": "Ala", "GCG": "Ala", "GCC": "Ala",
            "CAA": "Gln", "CAT": "His", "CAG": "Gln", "CAC": "His",
            "CTA": "Leu", "CTT": "Leu", "CTG": "Leu", "CTC": "Leu",
            "CGA": "Arg", "CGT": "Arg", "CGG": "Arg", "CGC": "Arg",
            "CCA": "Pro", "CCT": "Pro", "CCG": "Pro", "CCC": "Pro"
        }
}
}
        '''
    )


def all_possible_codons():
    """
    ALl 64 codons in order. This is just a simplified function to ensure we
    get them all
    :return: a set of all 64 codons.
    """
    return {
        'AAA', 'AAC', 'AAG', 'AAT', 'ACA', 'ACC', 'ACG', 'ACT',
        'AGA', 'AGC', 'AGG', 'AGT', 'ATA', 'ATC', 'ATG', 'ATT',
        'CAA', 'CAC', 'CAG', 'CAT', 'CCA', 'CCC', 'CCG', 'CCT',
        'CGA', 'CGC', 'CGG', 'CGT', 'CTA', 'CTC', 'CTG', 'CTT',
        'GAA', 'GAC', 'GAG', 'GAT', 'GCA', 'GCC', 'GCG', 'GCT',
        'GGA', 'GGC', 'GGG', 'GGT', 'GTA', 'GTC', 'GTG', 'GTT',
        'TAA', 'TAC', 'TAG', 'TAT', 'TCA', 'TCC', 'TCG', 'TCT',
        'TGA', 'TGC', 'TGG', 'TGT', 'TTA', 'TTC', 'TTG', 'TTT'
    }


def three_letters_to_one_letter():
    """
    By default we use three letter amino acid encoding, just because.
    This provides a translation back to one letter
    :return: a dict of amino acid codes
    """
    return {
        "Ala": "A", "Arg": "R", "Asn": "N", "Asp": "D",
        "Cys": "C", "Gln": "Q", "Glu": "E", "Gly": "G",
        "His": "H", "Ile": "I", "Leu": "L", "Lys": "K",
        "Met": "M", "Phe": "F", "Pro": "P", "Ser": "S",
        "Thr": "T", "Trp": "W", "Tyr": "Y", "Val": "V",
        "Ter": "*"
    }


def translation_tables():
    """
    Get a list of the valid translation tables
    :return: a list of translation tables
    """

    codes = genetic_codes()
    return list(codes.keys())
