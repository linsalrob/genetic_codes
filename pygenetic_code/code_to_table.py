"""
Convert a genetic code to a json table
"""
import sys

from .Error import InvalidTranslationTable
from .genetic_code import genetic_codes

def code_to_table(translation_table):
    """
    Return the json object for this code
    :param genetic_code: the genetic code (either as an int or a string)
    :return: the json object
    """


    code = genetic_codes()
    if (str(translation_table)) in code:
        return code[str(translation_table)]
    else:
        raise InvalidTranslationTable(f"Translation table {translation_table} is not defined")

def codons():
    """

    :return:
    """

