#!/usr/bin/python
# Usage python merge_output.py <count dt length output file> <get top-hits output file>
# Python program to merge the top-hit annotation information from different databases

import sys

def delete_dtseq():
    dtFile = open(sys.argv[1], 'r')
    inFile1 = open(sys.argv[2], 'r')
    outFile = open("merge_output.txt", 'w')

    dt_base = []
    tr1 = []
    ptr_base = 0
    ptr1 = 0
    for line in dtFile.readlines():
        dt_base.append(line.strip())      
    for line in inFile1.readlines():
        tr1.append(line.strip()) 

    while ptr_base < len(dt_base):
        tmp_line = dt_base[ptr_base]
        if tmp_line.split('\t')[0] == tr1[ptr1].split('\t')[0]:
            div = '%2.2f' % (float(tmp_line.split('\t')[-1]) / float(tr1[ptr1].split('\t')[-1]))
            if float(div) >= 0.8:
                print div
                tmp_line = tmp_line + '\t' + tr1[ptr1].split('\t', 1)[-1] + '\t' + str(div)
                outFile.write(tmp_line + '\n')
            if ptr1 < len(tr1) - 1:
                ptr1 = ptr1 + 1

        ptr_base = ptr_base + 1

    dtFile.close()
    inFile1.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    delete_dtseq()
    print 'I am DONE. Please check the output. :)'

