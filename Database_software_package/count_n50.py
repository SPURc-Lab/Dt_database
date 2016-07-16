#!/usr/bin/python
# Usage: python count_n50.py <Dt_database.fasta>
# Python program to calculate n50 from a transcriptome database

import sys

def delete_dtseq():
    inFile = open(sys.argv[1], 'r')
    outFile = open("n50.txt", 'w')

    dt_len = []
    for line in inFile.readlines():
        dt_len.append([line.split()[0], int(line.split()[1])])

    dt_len.sort(key=lambda x: (-x[1]))

    sum = 0
    for item in dt_len:
        sum = sum + item[1]
    sum = sum / 2
    print sum

    temp_sum = 0
    for item in dt_len:
        temp_sum = temp_sum + item[1]
        if temp_sum >= sum:
            print item[0] + '\t' + str(item[1])
            break
 
    inFile.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    delete_dtseq()
    print 'I am DONE. Please check the output. :)'
