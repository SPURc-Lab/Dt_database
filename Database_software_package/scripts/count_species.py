#!/usr/bin/python
# Usage python count_species.py <Dt_database.fasta>
# Python program to count speceis identification for annotation

import sys

def get_geneid():
    inFile = open(sys.argv[1], 'r')
    outFile = open("output.txt", 'w')

    dict = {}
    for line in inFile.readlines():
        name = line.split('[')[-1].split(']')[0]
        if name in dict:
            dict[name] = dict[name] + 1 
        else:
            dict[name] = 1

    dict = sorted(dict.items(), key=lambda x: x[1])
    for k in dict:
        outFile.write(k[0] + '\t' + str(k[1]) + '\n')

    inFile.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    get_geneid()
    print 'I am DONE. Please check the output. :)'
