#!/usr/bin/python
# Usage python get_redundant.py <merge_output.txt>
# Python program to extract the top hit of the Dt contig name for each transcriptID of the reference species.
# 1. Best E Value (the lowest E Value), then
# 2. Longest length of the sequence
# and the non top-hit Dt names would be generated in deleted_dtnames.txt

import sys

array = [] 

def gene_model():
    inFile = open(sys.argv[1], 'r')
    dtFile = open('deleted_dtnames.txt', 'w')

    count = 0
    for line in inFile.readlines():
        array.append([line.strip().split('\t')[0], line.strip().split('\t')[2], float(line.strip().split('\t')[-3]), float(line.strip().split('\t')[-1])])
    
    array.sort(key=lambda x: (x[1], x[2], -x[3]))
 
    current_crname = 'cr_name'
    for item in array:
        if current_crname != item[1]:
            print item
            current_crname = item[1]
        else:
            dtFile.write(item[0] + '\n')

    inFile.close()
    dtFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    gene_model()
    print 'I am DONE. Please check the output. :)'
