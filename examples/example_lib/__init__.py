"""
A simple library to help with the example code.

Most of this is abstracted from EdwardsLab and you might want to use the originals there. This
example libary is just so we don't pollute the pygenetic code library with other code.
"""

from .read_fasta import stream_fasta
from .stats import median, mean

__all__ = ['stream_fasta', 'mean', 'median']
