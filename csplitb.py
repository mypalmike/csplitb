#!/usr/bin/env python

import argparse
import binascii
import mmap
import sys

class CSplitB(object):
    def __init__(self, spliton, infile, number, prefix, suffix):
        spliton_str = binascii.unhexlify(spliton)
        if not prefix:
            prefix = "xx"
        if not suffix:
            suffix = ".dat"
        self.spliton_str = spliton_str
        self.infile = infile
        self.number = number
        self.prefix = prefix
        self.suffix = suffix
        self.number_fmt = "%%0%dd" % self.number
        self.last_idx = -1
        self.count = 0

    def run(self):
        with open(self.infile, "r+b") as f:
            self.mm = mmap.mmap(f.fileno(), 0)
            while True:
                idx = self.mm.find(self.spliton_str, self.last_idx + 1)
                if idx == -1:
                    self.finish()
                    break
                else:
                    self.rotate(idx)

    def rotate(self, idx):
        if self.last_idx != -1:
            self.write(self.mm[self.last_idx:idx])
        self.last_idx = idx


    def finish(self):
        self.write(self.mm[self.last_idx:])

    def write(self, data):
        outfile = self.prefix + (self.number_fmt % self.count) + self.suffix
        with open(outfile, "w+b") as f:
            f.write(data)
        self.count += 1


def main(argv = sys.argv):
    parser = argparse.ArgumentParser(description="csplitb - Context splitter on binary data.")
    parser.add_argument("spliton", help="Hexadecimal representation of data to split on.")
    parser.add_argument("infile", help="Input file.")
    parser.add_argument("-n", "--number", type=int, help="Number of zeroes to pad filename. Default is 2")
    parser.add_argument("-f", "--prefix", help="Output file prefix. Default is xx")
    parser.add_argument("-s", "--suffix", help="Output file suffix. Default is .dat")
    args = parser.parse_args(argv[1:])

    csplitb = CSplitB(args.spliton, args.infile, args.number, args.prefix, args.suffix)
    return csplitb.run()

if __name__ == '__main__':
    main()
