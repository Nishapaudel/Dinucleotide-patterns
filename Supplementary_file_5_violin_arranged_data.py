import os
import sys

file = sys.argv[1]
#file = 'home/nisha/Desktop/Di.. Homo_sapiens_exons.txt'
print('Dinucleotide', 'ratio', sep= '\t')

with open (file) as fh:
    header = fh.readline()
    for line in fh:
        columns = line.strip().split('\t')
        

        TpG =float(columns[10])
        print( 'TpG' , TpG, sep = '\t')
        CpA =float(columns[16])
        print( 'CpA' , CpA, sep = '\t')
        
        ApG =float(columns[6])
        print( 'ApG' , ApG, sep = '\t')
        CpT =float(columns[17])
        print( 'CpT' , CpT, sep = '\t')

        GpA =float(columns[12])
        print( 'GpA' , GpA, sep = '\t')
        TpC =float(columns[11])
        print( 'TpC' , TpC, sep = '\t')

        ApC =float(columns[7])
        print( 'ApC' , ApC, sep = '\t')
        GpT =float(columns[13])
        print( 'GpT' , GpT, sep = '\t')

        CpC =float(columns[19])
        print( 'CpC' , CpC, sep = '\t')
        GpG =float(columns[14])
        print( 'GpG' , GpG, sep = '\t')

        ApA =float(columns[4])
        print( 'ApA' , ApA, sep = '\t')
        TpT =float(columns[9])
        print( 'TpT' , TpT, sep = '\t')

        ApT =float(columns[5])
        print( 'ApT' , ApT, sep = '\t')
        
        

        TpA =float(columns[8])
        print( 'TpA' , TpA, sep = '\t')
        
        
        
        CpG =float(columns[18])
        print( 'CpG' , CpG, sep = '\t')
        
        
        
        GpC =float(columns[15])
        print( 'GpC' , GpC, sep = '\t')

        
        
        
        


        
