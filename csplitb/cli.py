#!/usr/bin/env python

import argparse
import sys

from csplitb import CSplitB


def main(argv = sys.argv):
    parser = argparse.ArgumentParser(description="csplitb - Context splitter on binary data.")
    parser.add_argument("spliton", help="Hexadecimal representation of data to split on.")
    parser.add_argument("infile", help="Input file.")
    parser.add_argument("-n", "--number", type=int, help="Number of zeroes to pad filename. Default is 2", default=2)
    parser.add_argument("-f", "--prefix", help="Output file prefix. Default is xx", default="xx")
    parser.add_argument("-s", "--suffix", help="Output file suffix. Defaults is .dat", default=".dat")
    parser.add_argument("-a", "--ascii", action="store_true", help="Treat spliton as ASCII text instead of hexadecimal.")
    parser.add_argument("-k", "--keep-first", action="store_true", help="Store data prior to the first match as the first output file.")
    args = parser.parse_args(argv[1:])

    spliton = args.spliton
    if args.ascii:
        spliton = spliton.encode().hex()

    csplitb = CSplitB(spliton, args.infile, args.number, args.prefix, args.suffix, args.keep_first)
    return csplitb.run()


if __name__ == '__main__':
    main()
