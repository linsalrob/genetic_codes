"""
Custom exceptions for genetic code parsing
"""

class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidTranslationTable(Exception):
    """The translation table is not defined"""

    def __init__(self, message):
        self.message = message
