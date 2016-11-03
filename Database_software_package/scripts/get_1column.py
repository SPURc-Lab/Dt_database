#!/usr/bin/python
# Usage python get_1column.py <toptophit sequence>
# Python program to extract the name of toptophit sequences 

import sys


def get_geneid():
    inFile = open(sys.argv[1], 'r')
    outFile = open("top_1_column.txt", 'w')

    for line in inFile:
        tmp_line = line.strip().split("'")[1]
        outFile.write(tmp_line + '\n')
		inFile.close()
        outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    get_geneid()
    print 'I am Done. Please check the output. :)'
