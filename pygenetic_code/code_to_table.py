"""
Convert a genetic code to a json table
"""

from .error import InvalidTranslationTableException
from .genetic_code import genetic_codes, all_possible_codons


def code_to_table(translation_table):
    """
    Return a dictionary for this genetic code. The dictionary has two entries, 'initiators' which are the start
    codons, and 'codons' that are the genetic code.

    :param genetic_code: the genetic code (either as an int or a string)
    :return: the json object
    """

    code = genetic_codes()
    if str(translation_table) in code:
        return code[str(translation_table)]
    raise InvalidTranslationTableException(f"Translation table {translation_table} is not defined")


def codons_to_translation_tables():
    """
    Get a dictionary of all the codons, with the values being a dictionary of translation tables and their encodings
    :return: a dictionary of dictionaries
    """

    code = genetic_codes()
    codons = {x:{} for x in all_possible_codons()}
    for i in code:
        for cd in code[i]['codons']:
            codons[cd][i] = code[i]['codons'][cd]
    return codons
