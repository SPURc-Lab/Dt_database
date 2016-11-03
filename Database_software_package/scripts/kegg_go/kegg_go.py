#!/usr/bin/python
# Usage: python kegg_go.py <merge_output.txt>
# Python program to get kegg_gene, kegg_ortology, gene_ontology, and gene_ontology definition from online URL

import sys
import urllib2

def get_kegg():
    inFile = open(sys.argv[1], 'r')
    outFile = open("kegg_go_output.txt", 'w')

    inBase = []
    for line in inFile.readlines():
        inBase.append([line.split()[2], line.strip()])

    total = len(inBase)
    count = 0
    for item in inBase:
        # NCBI_Protein ID to KEGG genes
        print '%d / %d' %(count, total)
        count = count + 1
        kegg_gene = urllib2.urlopen('http://rest.kegg.jp/conv/genes/ncbi-proteinid:' + item[0].split('.')[0]).read().strip()
        if kegg_gene != '':
            kegg_gene = kegg_gene.split()[1]

            # KEGG genes to KEGG orthology
            kegg_org = urllib2.urlopen('http://rest.kegg.jp/link/orthology/' + kegg_gene).read().strip()
            if kegg_org != '':
                # KO to GO
                kegg_go = urllib2.urlopen('http://www.genome.jp/dbget-bin/get_linkdb?-t+go+ko:' + kegg_org.replace('ko:','').split()[1]).readlines()
                output_str = ''
                for i in kegg_go:
                    if 'amigo.geneontology.org' in i:
                        go = i.split('"')[1].split('/')[-1]
                        define = i.split('>')[-1].strip()
                        output_str = output_str + '\t%s\t%s' %(go, define)
                outFile.write(item[1] + '\t' + kegg_gene + '\t' + kegg_org.replace('ko:','').split()[1] + output_str + '\n')
            else:
                outFile.write(item[1] + '\t' + kegg_gene + '\t'  + '\n')
        else:
            #print item[0] + ': no kegg gene found...'
            outFile.write(item[1] + '\t\t\n')

    inFile.close()
    outFile.close()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Invalid arguments!\n'
        sys.exit(0)

    get_kegg()
    print 'I am DONE. Please check the output. :)'
