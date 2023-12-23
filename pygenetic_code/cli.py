"""
Runnable entry point to use as a standalone script
"""

import argparse
from .print_codes import print_json, print_difference_to_code_one, print_difference_to_maximum
from .version import __version__

__author__ = 'Rob Edwards'


def run():
    """
    Parse command line arguments and run the code
    :return: None
    """
    parser = argparse.ArgumentParser(description='genetic_codes for translation tables')
    parser.add_argument('-j', '--json', help='print the genetic codes as a json object', action='store_true')
    parser.add_argument('-d', '--difference', action='store_true',
                        help='print the genetic code as the difference from translation table 1')
    parser.add_argument('-x', '--maxdifference', action='store_true',
                        help='print difference from the most common codon usage')
    parser.add_argument('-v', '--version', help='print the version', action='store_true')
    args = parser.parse_args()

    if args.json:
        print_json()

    if args.difference:
        print_difference_to_code_one()

    if args.maxdifference:
        print_difference_to_maximum()

    if args.version:
        print(__version__)
