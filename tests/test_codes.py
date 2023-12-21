"""

"""

import os
import sys
import argparse

__author__ = 'Rob Edwards'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=' ')
    parser.add_argument('-f', help='input file', required=True)
    parser.add_argument('-v', help='verbose output', action='store_true')
    args = parser.parse_args()