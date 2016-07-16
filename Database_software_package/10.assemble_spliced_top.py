#!/usr/bin/python
# Usage python assemble_spliced_top.py <spliced.txt> from different species
# Python program to assemble the potential alternative splicing variant hits from the top-hit different species

import sys

def get_geneid():
    fastaFile = open(sys.argv[1], 'r')
    specFile1 = open(sys.argv[2], 'r')
    specFile2 = open(sys.argv[3], 'r')
    specFile3 = open(sys.argv[4], 'r')
    specFile4 = open(sys.argv[5], 'r')
    outFile = open("output.txt", 'w')

    dt_names = []
    for line in fastaFile:
        if '>' in line:
            dt_names.append(line.split()[0].split('>')[-1])

    spec1_names = {}
    spec2_names = {}
    spec3_names = {}
    spec4_names = {}
    for line in specFile1:
        spec1_names[line.strip().split()[-1]] = line.split()[0]
    for line in specFile2:
        spec2_names[line.strip().split()[-1]] = line.split()[0]
    for line in specFile3:
        spec3_names[line.strip().split()[-1]] = line.split()[0]
    for line in specFile4:
        spec4_names[line.strip().split()[-1]] = line.split()[0]

    for dt_name in dt_names:
        out_str = dt_name

        out_str = out_str + '\t'
        if dt_name in spec1_names:
            out_str = out_str + spec1_names[dt_name]

        out_str = out_str + '\t'
        if dt_name in spec2_names:
            out_str = out_str + spec2_names[dt_name]
        
        out_str = out_str + '\t'
        if dt_name in spec3_names:
            out_str = out_str + spec3_names[dt_name]

        out_str = out_str + '\t'
        if dt_name in spec4_names:
            out_str = out_str + spec4_names[dt_name]

        outFile.write(out_str + '\n')        

    fastaFile.close()
    specFile1.close()
    specFile2.close()
    specFile3.close()
    specFile4.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    get_geneid()
    print 'I am DONE. Please check the output. :)'
