"""
Custom exceptions for genetic code parsing
"""

class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidTranslationTableException(Exception):
    """The translation table is not defined"""

    def __init__(self, message):
        self.message = message


class InvalidCodonException(Exception):
    """The codon is not valid"""

    def __init__(self, message):
        self.message = message
