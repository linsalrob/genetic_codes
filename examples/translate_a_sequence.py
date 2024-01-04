"""
Example code to translate a sequence using a different translation table

For example, if you create an ORF caller, and want to convert DNA->protein, you might use this method
"""

import PyGeneticCode


if __name__ == "__main__":
    dnaseq="ATCGATCGTCAGCATGCATCGCATCGAGCTCGTACGATCGACTAGCTACGCTACGTACGACTACGCTAGCATCGATCAGCATCACTATCGCTAGCTACGATCTATAA"
    print(f"DNA sequence: {dnaseq}\nProtein seq : {PyGeneticCode.translate(dnaseq, 11)}")
