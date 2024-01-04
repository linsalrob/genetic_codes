"""
Runnable entry point to use as a standalone script
"""

import argparse
import sys

from .translations import translate, six_frame_translation
from .print_codes import print_json, print_difference_to_code_one, print_difference_to_maximum
from .version import __version__

__author__ = 'Rob Edwards'


def run():
    """
    Parse command line arguments and run the code
    :return: None
    """
    parser = argparse.ArgumentParser(description='genetic_codes for translation tables', add_help=False)

    translator = parser.add_argument_group('translating sequences')
    translator.add_argument('-t', '--translate', help='translate a sequence in one reading frame')
    translator.add_argument('-s', '--sixframe', help='translate a sequence in all six reading frames')
    translator.add_argument('-c', '--translationtable', default=11, type=int,
                           help='translation table to use (default == 11)')
    translator.add_argument('--minlen', default=3, type=int,
                            help='minimum ORF length for the six frame translation (default=3)')
    translator.add_argument('--threads', default=8, type=int,
                            help='number of threads to use for the six frame translation (default=8)')

    printing = parser.add_argument_group("printing genetic codes")
    printing.add_argument('-j', '--json', help='print the genetic codes as a json object', action='store_true')
    printing.add_argument('-d', '--difference', action='store_true',
                        help='print the genetic code as the difference from translation table 1')
    printing.add_argument('-x', '--maxdifference', action='store_true',
                        help='print difference from the most common codon usage')

    optional = parser.add_argument_group('optional arguments')
    optional.add_argument("-h", "--help", action="help", help="show this help message and exit")
    optional.add_argument('-v', '--version', help='print the version', action='store_true')
    optional.add_argument('--verbose', help='debugging level output', action='store_true')
    args = parser.parse_args()

    if args.translate:
        print(translate(args.translate, args.translationtable, args.verbose))
        sys.exit(0)

    if args.sixframe:
        sf = six_frame_translation(args.sixframe, args.translationtable, args.threads, args.verbose)
        for seqid in sf:
            if len(sf[seqid]) > args.minlen:
                print(f">{seqid}\n{sf[seqid]}")
        sys.exit(0)

    if args.json:
        print_json()
        sys.exit(0)

    if args.difference:
        print_difference_to_code_one()
        sys.exit(0)

    if args.maxdifference:
        print_difference_to_maximum()
        sys.exit(0)

    if args.version:
        print(__version__)
        sys.exit(0)

    parser.print_help()
