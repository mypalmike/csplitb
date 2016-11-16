#!/usr/bin/env python

import binascii
import mmap


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
