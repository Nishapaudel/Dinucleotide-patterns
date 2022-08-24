import os
import sys

file = sys.argv[1]
#file = 'MT_gene_ratio'
print('Dinucleotide', 'ratio', sep= '\t')

with open (file) as fh:
    header = fh.readline()
    for line in fh:
        columns = line.strip().split('\t')
        #print(columns)

        TpG =float(columns[5])
        print( 'TpG' , TpG, sep = '\t')
        CpA =float(columns[6])
        print( 'CpA' , CpA, sep = '\t')
        
        ApG =float(columns[7])
        print( 'ApG' , ApG, sep = '\t')
        CpT =float(columns[8])
        print( 'CpT' , CpT, sep = '\t')

        GpA =float(columns[9])
        print( 'GpA' , GpA, sep = '\t')
        TpC =float(columns[10])
        print( 'TpC' , TpC, sep = '\t')

        ApC =float(columns[11])
        print( 'ApC' , ApC, sep = '\t')
        GpT =float(columns[12])
        print( 'GpT' , GpT, sep = '\t')

        CpC =float(columns[13])
        print( 'CpC' , CpC, sep = '\t')
        GpG =float(columns[14])
        print( 'GpG' , GpG, sep = '\t')

        ApA =float(columns[15])
        print( 'ApA' , ApA, sep = '\t')
        TpT =float(columns[16])
        print( 'TpT' , TpT, sep = '\t')

        ApT =float(columns[17])
        print( 'ApT' , ApT, sep = '\t')
        TpA =float(columns[18])
        print( 'TpA' , TpA, sep = '\t')
        
        CpG =float(columns[19])
        print( 'CpG' , CpG, sep = '\t')
        GpC =float(columns[20])
        print( 'GpC' , GpC, sep = '\t')
