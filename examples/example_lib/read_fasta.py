"""
A simple accessory library to stream a fasta file. The original is in EdwardsLab repo, but this just makes it standalone
"""

import gzip
import sys


def stream_fasta(fastafile, whole_id=True):
    """
    Stream a fasta file, one read at a time. Saves memory!

    :param fastafile: The fasta file to stream
    :type fastafile: str
    :param whole_id: Whether to return the whole id (default) or just up to the first white space
    :type whole_id:bool
    :return:A single read
    :rtype:str, str
    """

    try:
        if fastafile.endswith('.gz'):
            f = gzip.open(fastafile, 'rt')
        else:
            f = open(fastafile, 'r', encoding='utf-8')
    except IOError as e:
        print(f"There was an IO Error: {e}", file=sys.stderr)

    while f:
        # first line should start with >
        idline = f.readline()
        if not idline:
            break
        if not idline.startswith('>'):
            sys.exit(f"Do not have a fasta file at: {idline}")
        if not whole_id:
            idline = idline.split(" ")[0]
        idline = idline.strip().replace('>', '', 1)
        posn = f.tell()
        line = f.readline()
        seq = ""
        while not line.startswith('>'):
            seq += line.strip()
            posn = f.tell()
            line = f.readline()
            if not line:
                break
        f.seek(posn)
        yield idline, seq
