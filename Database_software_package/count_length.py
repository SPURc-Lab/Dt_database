#!/usr/bin/python
# Usage python count_length.py <Dt_database.fasta>
# Python program to count length for each individual contigs

import sys

def get_length():
    inFile = open(sys.argv[1], 'r')
    outFile = open("length_output.txt", 'w')

    dt_name = ''
    count = 0
    for line in inFile.readlines():
        if '>' in line:
            if count != 0:
                outFile.write(dt_name + '\t' + str(count) + '\n')
            dt_name = line.strip().split()[0].split('>')[-1]
            count = 0
        else:
            count = count + len(line.strip())
         
    outFile.write(dt_name + '\t' + str(count) + '\n')
    inFile.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    get_length()
    print 'I am DONE. Please check the output. :)'
