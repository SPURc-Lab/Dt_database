#!/usr/bin/python
# Usage python clustal.py <merge_output_txt> <Dt_combined_database.fasta>
# Python program to evaluate the similarity score of the redundant contigs versus the toptop-hit contigs using ClustalW 

import sys
import subprocess


def gene_model():
    inFile = open(sys.argv[1], 'r')
    fastaFile = open(sys.argv[2], 'r')
    dtFile = open('clustalw_output.txt', 'w')

    cr_names = [] 
    for line in inFile.readlines():
        cr_names.append([line.strip().split('\t')[0], line.strip().split('\t')[2], float(line.strip().split('\t')[-3]), float(line.strip().split('\t')[-1])]) 
    
    cr_names.sort(key=lambda x: (x[1], x[2],-x[3]))
 
    fastas = []
    temp_name = ''
    temp_fasta = ''
    for line in fastaFile.readlines():
        if '>' in line:
            if temp_name != '':
                fastas.append([temp_name, temp_fasta])
            temp_name = line.strip()
            temp_fasta = ''
        else:
            temp_fasta = temp_fasta + line.strip()
    
    current_crname = 'cr_name'
    top_name = ''
    top_fasta = ''
    count = 0
    for item in cr_names:
        if current_crname != item[1]:
            current_crname = item[1]
            top_name = item[0]
            found = False
            top_fasta = ''
            for index,fasta in enumerate(fastas):
                if item[0] == fasta[0].split()[0].split('>')[-1]:
                    top_fasta = fasta[0] + '\n' + fasta[1]
                    fastas.pop(index)
                    break
            count = count + 1
            print '%d: %s, %d: fastas left' %(count, current_crname, len(fastas))
        else:
            #
            # do clustal for the forward non-top sequence
            #

            # create the infile for clustalw from the fastaFile
            tempFile = open('temp_fasta.txt', 'w')
            found = False
            nontop_fasta = ''
            score1 = 0
            score2 = 0
            for index,fasta in enumerate(fastas):
                if item[0] == fasta[0].split()[0].split('>')[-1]:
                    nontop_fasta = fasta[0] + '\n' + fasta[1]
                    fastas.pop(index)
                    break
            tempFile.write(top_fasta + '\n' + nontop_fasta + '\n')
            tempFile.close()

            # execute clustalw2 program and output the score  
            clustalw_out = subprocess.Popen('../tools/clustalw-2.1/src/clustalw2 -INFILE=temp_fasta.txt -ALIGN', shell=True, stdout=subprocess.PIPE).stdout.readlines()
            for line in clustalw_out:
                if 'Sequences (1:2) Aligned.' in line:
                    score1 = int(line.split()[-1])

            #
            # do reverse clustalw for the non-top sequence
            #
             
            # create the infile for clustalw from the fastaFile
            tempFile = open('temp_fasta.txt', 'w')
            reverse_temp = nontop_fasta.split('\n')[-1][::-1]
            reverse_temp = reverse_temp.replace('A', 'X').replace('T', 'A').replace('X', 'T')
            reverse_temp = reverse_temp.replace('C', 'X').replace('G', 'C').replace('X', 'G')
            reverse_nontop_fasta = nontop_fasta.split('\n')[0] + '\n' + reverse_temp
            tempFile.write(top_fasta + '\n' + reverse_nontop_fasta + '\n')
            tempFile.close()

            # execute clustalw2 program and output the score
            clustalw_out = subprocess.Popen('../tools/clustalw-2.1/src/clustalw2 -INFILE=temp_fasta.txt -ALIGN', shell=True, stdout=subprocess.PIPE).stdout.readlines()
            for line in clustalw_out:
                if 'Sequences (1:2) Aligned.' in line:
                    score2 = int(line.split()[-1])
                    if score1 >= score2:
                        dtFile.write(top_name + '\t' + item[0] + '\t' + str(score1) + '\n')
                    else:
                        dtFile.write(top_name + '\t' + item[0] + '\t' + str(score2) + '\n')

    inFile.close()
    dtFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    gene_model()
    print 'I am DONE. Please check the output. :)'
