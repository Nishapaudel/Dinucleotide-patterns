# import all modules
import sys
import os

#setting up all variables
NCBI_file = sys.argv[1] # refseq list (supplementary file 2) from NCBI website https://ftp.ncbi.nlm.nih.gov/genomes/refseq/

with open (NCBI_file) as fh:
    for line in fh:
        if line.startswith('#'):
            continue
        content = line.strip().split('\t')
        print(content)
        name = content[-4]
        print(name)
        depth_name = name.split('/')
        print(depth_name)
        depth_name_last = depth_name[-1]
        animal_name = content[7]
        #print(depth_name_last)
        new = animal_name, replace ' ', '_')
        print(new)
        command1 = 'wget ' + name +'/' +  depth_name_last + '_genomic.fna.gz' # for ggf file write gff inplace of fna
        #print(command1)
        #os.system(command1)      
        print("Run completed for ",end='\t')
        print(animal_name)