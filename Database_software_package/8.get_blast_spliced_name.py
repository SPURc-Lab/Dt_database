#!/usr/bin/python
# Usage python get_blast_spliced_name.py <blast output file>
# <blast output file> the blast_output.txt generated from BLASTX with alternative splicing variants with related speceis using Dt redundant contigs
# Python program to extract the potential alternative splicing variants of Dt

import sys


def get_geneid():
    inFile = open(sys.argv[1], 'r')
    outFile = open("spliced.txt", 'w')

    outer_query = False
    inner_query = False
    first_newline = False
    tophit = False
    protein_name = ''
    for line in inFile.readlines():
        if outer_query == True and inner_query == True:
             if first_newline == True:
                 if tophit == True:
                     outer_query = False
                     inner_query = False
                     first_newline = False
                     tophit = False
                     continue
                 else:
                     dt_name = line.split()[0]
                     outFile.write(protein_name + '\t' + dt_name + '\t' + '\n') 
                     tophit = True
             elif line == '\n' and first_newline == False:
                 first_newline = True           
 
        elif outer_query == True and 'Sequences producing significant alignments' in line:
            inner_query = True
        elif 'Query=' in line:
            protein_name = line.strip().split()[1]
            outer_query = True
         
    inFile.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    get_geneid()
    print 'I am DONE. Please check the output. :)'
