"""
Convert a genetic code to a json table
"""

from genetic_code import genetic_codes

def code_to_table(translation_table):
    """
    Return the json object for this code
    :param genetic_code: the genetic code (either as an int or a string)
    :return: the json object
    """

    try:
        code = genetic_codes(str(translation_table))
    except KeyError as e:



