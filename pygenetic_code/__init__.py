from .genetic_code import genetic_codes, all_possible_codons
from .code_to_table import code_to_table, codons_to_translation_tables
from .translate import translate

__all__ = [
    'genetic_codes', 'all_possible_codons',
    'code_to_table', 'codons_to_translation_tables',
    'translate'
]