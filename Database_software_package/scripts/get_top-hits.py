#!/usr/bin/python
# Usage python get_top-hits.py <blast output file>
# <blast output file> the blast_output.txt generated from MPIBlast, protein database from all bacterial and plants on Mar,14,2016 available at ftp://ftp.ncbi.nlm.nih.gov/refseq/release/
# <output.txt> as the output
# Python program to extract the top-hits of ncbi_proteinid

import sys


def get_geneid():
    inFile = open(sys.argv[1], 'r')
    outFile = open("output.txt", 'w')

    name_query = False
    outer_query = False
    inner_query = False
    evalue_query = False
    func_query = False
    dt_name = ''
    transcriptID = ''
    evalue = ''
    func_name = ''
    length = ''
    for line in inFile:
        if outer_query == True and inner_query == True and evalue_query == True:
            if 'Length' in line:
                if evalue[0] == 'e':
                    evalue = '1' + evalue 
                length = line.strip().split()[-1]
                if float(evalue) <= float('1e-10'):
                    outFile.write(dt_name + '\t' + transcriptID + '\t' + func_name + '\t'  + evalue + '\t' + length + '\n')
                outer_query = False
                inner_query = False
                evalue_query = False
                func_query = False
                extra_query = False
                continue
            elif func_query == True:
                func_name = func_name + line.strip()
            elif line.startswith('>'):
                transcriptID = line.split('|')[1]
                func_name = line.split('|')[2].strip()
                func_query = True

        elif outer_query == True and inner_query == True:
            line = next(inFile)
            evalue = line.split()[-1]
            evalue_query = True
        elif outer_query == True and 'Sequences producing significant alignments' in line:
            inner_query = True
        elif 'Query=' in line:
            dt_name = line.strip().split()[1]
            outer_query = True
         
    inFile.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    get_geneid()
    print 'I am DONE. Please check the output. :)'
