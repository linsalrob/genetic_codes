"""
pygenetic_code

Access to genetic translation tables and codon translations for different genetic codes.
"""

from .genetic_code import genetic_codes, all_possible_codons, translation_tables
from .code_to_table import code_to_table, codons_to_translation_tables
from .translations import translate_codon, six_frame_translation, translate
from .dna_and_rna import dna_to_rna, rna_to_dna
from .version import __version__

__all__ = [
    'genetic_codes', 'all_possible_codons', 'translation_tables',
    'code_to_table', 'codons_to_translation_tables',
    'translate_codon', 'six_frame_translation', 'translate',
    'dna_to_rna', 'rna_to_dna',
    '__version__'
    ]
