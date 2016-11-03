#!/usr/bin/python
# Usage python count_atcg.py <Dt_database.fasta>
# Python program to count atcg percentage for the database

import sys

def get_geneid():
    inFile = open(sys.argv[1], 'r')
    outFile = open("output.txt", 'w')

    atcg = [0, 0, 0, 0]
    for line in inFile:
        if '>' not in line:
            for ch in line.strip():
                if ch == 'A':
                    atcg[0] = atcg[0] + 1 
                elif ch == 'T':
                    atcg[1] = atcg[1] + 1 
                elif ch == 'C':
                    atcg[2] = atcg[2] + 1 
                elif ch == 'G':
                    atcg[3] = atcg[3] + 1 

    sum = float(atcg[0] + atcg[1] + atcg[2] + atcg[3])
    print atcg[0]
    print atcg[1]
    print atcg[2]
    print atcg[3]
    print 'A:%.3f, T:%.3f, C:%.3f, G:%.3f' %(atcg[0]/sum, atcg[1]/sum, atcg[2]/sum, atcg[3]/sum)
         
    inFile.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    get_geneid()
    print 'I am DONE. Please check the output. :)'
