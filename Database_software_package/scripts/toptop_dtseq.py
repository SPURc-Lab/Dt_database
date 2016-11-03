#!/usr/bin/python
# Usage python top_dtseq.py <Dt_combined_database.fasta> <deleted_dtnames.txt>
# Python program to delete non-redundant contigs from the combined big database in fasta format.

import sys

def delete_dtseq():
    inFile = open(sys.argv[1], 'r')
    dtFile = open(sys.argv[2], 'r')
    outFile = open("Dt_toptop-hit_seq.fa", 'w')

    dt_names = []
    fasta = []
    for line in dtFile.readlines():
       dt_names.append(line.strip().split('\t')[0])

    dt_names.sort()

    temp_name = ''
    temp_fasta = ''
    for line in inFile.readlines():
        if '>' in line: 
            if temp_name != '':
                fasta.append([temp_name.split()[0].split('>')[-1], temp_name, temp_fasta])
            temp_name = line.strip()
            temp_fasta = ''
        else:
            temp_fasta = temp_fasta + line.strip()

    fasta.append([temp_name.split()[0].split('>')[-1], temp_name, temp_fasta])
    fasta.sort(key=lambda x: (x[0]))

    fa_index = 0
    for dt_index,item in enumerate(dt_names):
        #print item
        while fasta[fa_index][0] != item:
            if fa_index < len(fasta) - 1:
                fa_index = fa_index + 1 
        if fa_index == len(fasta):
            #print "Not found!"
            exit(0)
        else:
            #print "Found!"
            outFile.write(fasta[fa_index][1] + '\n' + fasta[fa_index][2] + '\n')

    inFile.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    delete_dtseq()
    print 'I am DONE. Please check the output. :)'
