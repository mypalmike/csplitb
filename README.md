# csplitb

Command-line tool like unix csplit but which splits binary files based on content boundaries rather than index boundaries.

This was originally written to salvage jpegs from a corrupted disk image.

## Example usage:

$ csplitb --prefix photo --suffix .jpg --number 4 ffd8ffe1 corrupted-disk-image.raw

This will split the disk image, keeping the header, into photo0000.jpg, photo0001.jpg, etc. Because a disk image represents a potentially fragmented file system, some (or all) of the jpeg files may be corrupted.

The "ffd8ffe1" here is a jpeg header. I'm not an expert on the jpeg format, so it's possible that you may need to use a different hex search term. Use a hex editor or viewer such as xxd to find what content you want to split on.

## Installation

pip install csplitb

## Basic Test

Either of the following should create xx00.dat through xx18.dat, each starting with "MARKER".

`csplitb 4D41524B4552 testdata.txt  # 4D41524B4552 is hexadecimal for "MARKER"`

`csplitb --ascii MARKER testdata.txt`

## Technical details

This script is a fairly minimal wrapper around Python's standard library mmap (memory mapped files) find method. Because of this, it *should* work with very large files and be near optimal performance-wise. But its reliability and speed is dependent on the operating system's and Python's implementation memory mapping implementation.
