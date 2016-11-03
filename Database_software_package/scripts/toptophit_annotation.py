#!/usr/bin/python
# Usage python toptophit_annotation.py <merge_output.txt>
# Python program to extract the non-redundant annotation information.

import sys

array = [] 

def gene_model():
    inFile = open(sys.argv[1], 'r')
    outFile = open('merge_output_tt.txt', 'w')

    count = 0
    for line in inFile.readlines():
        array.append([line.strip(), line.strip().split('\t')[2], float(line.strip().split('\t')[-3]), float(line.strip().split('\t')[-1])])
    
    array.sort(key=lambda x: (x[1], x[2], -x[3]))
 
    current_crname = 'cr_name'
    for item in array:
        if current_crname != item[1]:
            current_crname = item[1]
            outFile.write(item[0] + '\n')

    inFile.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    gene_model()
    print 'I am DONE. Please check the output. :)'
