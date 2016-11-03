#!/usr/bin/python
# Usage python unique_go.py <merge_output_tt.txt>
# Python program to extract unique go ID from non-redundant top-hit contig annotation file

import sys

def get_geneid():
    inFile = open(sys.argv[1], 'r')
    outFile = open("output.txt", 'w')

    dict_go2dt = {}
    dict_go2def = {}
    for line in inFile.readlines():
        names = []
        if 'GO:' in line:
            names = line.split('GO:')
            names.pop(0)

            for name in names:
                go_name =  name.split()[0]
                dict_go2def[go_name] = name.strip().split('\t')[-1]
                if go_name in dict_go2dt:
                    dict_go2dt[go_name] = dict_go2dt[go_name] + '\t' + line.split()[0] 
                else:
                    dict_go2dt[go_name] = line.split()[0]

    for key in dict_go2dt:
        outFile.write('GO:' + key + '\t' + dict_go2def[key] + '\t' + dict_go2dt[key] + '\n')

    inFile.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    get_geneid()
    print 'I am DONE. Please check the output. :)'
