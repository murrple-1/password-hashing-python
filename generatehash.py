#!/usr/bin/env python

import sys

import passwordhash

def main():
    args = sys.argv
    if len(args) < 2:
        print 'Usage: {0} [PASSWORD]'.format(args[0])
        sys.exit(1)

    print passwordhash.create_hash(args[1])

if __name__ == "__main__":
    main()

