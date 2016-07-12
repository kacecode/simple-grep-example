#! /usr/bin/env python

import argparse
import sys

# Use standard tools to parse input rather than do it ourselves.
parser = argparse.ArgumentParser(
    description='Prints lines from passed in file that match the search term.')
parser.add_argument('pattern', type=str, help='The string to search for')
parser.add_argument('file', type=argparse.FileType('r'), nargs='?',
                    help='The input to search in', default=sys.stdin)

# Resolve the arguments sent to us by the commandline.
args = parser.parse_args()


def grep(pattern, source):
    # Return a list of strings where the pattern is found.
    # Remove trailing newline from the input string.
    return [line.rstrip() for line in source if line.find(pattern) != -1]


# What to do if this file is called by the commandline.
# (Instead of another area of python.)
if __name__ == "__main__":
    results = grep(args.pattern, args.file)
    for result in results:
        print(result)
